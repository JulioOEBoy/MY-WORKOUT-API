from fastapi import FastAPI, Depends, HTTPException, Query
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session
from fastapi_pagination import Page, paginate, add_pagination
from pydantic import BaseModel
from typing import Optional
from database import Base, engine, SessionLocal
from models import Atleta as AtletaModel

app = FastAPI(title="Workout API")

Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

class AtletaCreate(BaseModel):
    nome: str
    cpf: str
    centro_treinamento: str
    categoria: str

class AtletaOut(BaseModel):
    nome: str
    centro_treinamento: str
    categoria: str

    class Config:
        orm_mode = True

@app.post("/atletas", status_code=201)
def criar_atleta(atleta: AtletaCreate, db: Session = Depends(get_db)):
    novo_atleta = AtletaModel(**atleta.dict())
    try:
        db.add(novo_atleta)
        db.commit()
        db.refresh(novo_atleta)
        return {"message": "Atleta cadastrado com sucesso!"}
    except IntegrityError:
        db.rollback()
        raise HTTPException(
            status_code=303,
            detail=f"Já existe um atleta cadastrado com o cpf: {atleta.cpf}"
        )

@app.get("/atletas", response_model=Page[AtletaOut])
def listar_atletas(
    nome: Optional[str] = Query(None),
    cpf: Optional[str] = Query(None),
    db: Session = Depends(get_db)
):
    query = db.query(AtletaModel)
    if nome:
        query = query.filter(AtletaModel.nome.ilike(f"%{nome}%"))
    if cpf:
        query = query.filter(AtletaModel.cpf == cpf)
    return paginate(query.all())

add_pagination(app)
