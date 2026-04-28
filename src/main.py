import random
from fastapi import FastAPI # type: ignore
from pydantic import BaseModel # type: ignore

app = FastAPI()


class Estudante(BaseModel):
    nome: str
    idade: str
    curso: bool


@app.get("/helloworld")
async def root():
    return {"message": "Hello World"}


@app.get("/funcaoteste")
async def funcaoteste():
    return {"teste": True, "numero": random.randint(1, 100)}


@app.post("/estudante/cadastrar")
async def cadastrar_estudante(estudante: Estudante):
    return {"message": f"Estudante {estudante.nome} cadastrado com sucesso!"}


@app.put("/estudante/atualizar/{nome}")
async def atualizar_estudante(nome: str, estudante: Estudante):
    return {"message": f"Estudante {nome} atualizado para {estudante.nome} com sucesso!"}

@app.delete("/estudante/deletar/{nome}")
async def deletar_estudante(nome: str):
    return {"message": f"Estudante {nome} deletado com sucesso!"}   

