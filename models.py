from sqlalchemy import Column, Integer, String, UniqueConstraint
from database import Base

class Atleta(Base):
    __tablename__ = "atletas"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, nullable=False)
    cpf = Column(String, unique=True, nullable=False)
    centro_treinamento = Column(String, nullable=False)
    categoria = Column(String, nullable=False)

    __table_args__ = (UniqueConstraint('cpf', name='uix_cpf'),)
