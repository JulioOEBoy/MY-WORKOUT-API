# 🏋️‍♂️ MY-WORKOUT-API

API REST construída com **FastAPI** para o gerenciamento de atletas, centros de treinamento e categorias. Projeto desenvolvido como parte de um desafio da DIO, com foco em boas práticas de API, banco de dados com SQLite e paginação de dados.

---

## ⚙️ Tecnologias Utilizadas

- Python 3.11+
- FastAPI
- SQLite
- SQLAlchemy
- Pydantic
- FastAPI Pagination

---

## 🚀 Como Rodar o Projeto Localmente

1. Clone o repositório:

```bash
git clone https://github.com/JulioOEboy/MY-WORKOUT-API.git
cd MY-WORKOUT-API
```

2. Crie e ative um ambiente virtual:

```bash
python -m venv venv
# Windows:
.\venv\Scripts\activate
# Linux/macOS:
source venv/bin/activate
```

3. Instale as dependências:

```bash
pip install -r requirements.txt
```

4. Execute o servidor:

```bash
uvicorn main:app --reload
```

5. Acesse a documentação da API:

- Swagger UI: [http://localhost:8000/docs](http://localhost:8000/docs)
- ReDoc: [http://localhost:8000/redoc](http://localhost:8000/redoc)

---

## 📌 Endpoints principais

- `GET /atletas` – Lista todos os atletas (paginado)
- `POST /atletas` – Cria um novo atleta
- `PUT /atletas/{id}` – Atualiza um atleta existente
- `DELETE /atletas/{id}` – Remove um atleta

---

## 🧠 Autor

Desenvolvido por **Júlio César Ferreira Pedrini**  
[GitHub @JulioOEboy](https://github.com/JulioOEboy)

---
