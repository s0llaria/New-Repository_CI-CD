from src.main import *
from unittest.mock import patch
import pytest

@pytest.mark.asyncio
async def test_root():
    result = await root()
    assert result == {"message": "Hello World"}


def test_funcaoteste():
    with patch('random.randint', return_value=42):
        result = funcaoteste()
    assert result == {"teste": True, "numero": 42}


def test_cadastrar_estudante():
    estudante_teste = Estudante(nome="João", idade="20", curso=True)
    result = create_estudante(estudante_teste)
    assert estudante_teste == result


def test_update_estudante_positivo():
    result = update_estudante(10)
    assert not result


def test_update_estudante_negativo():
    result = update_estudante(-5)
    assert not result


def test_delete_estudante_positivo():
    result = delete_estudante(10)
    assert not result


class Estudante(BaseModel):
    nome: str
    idade: str
    curso: bool