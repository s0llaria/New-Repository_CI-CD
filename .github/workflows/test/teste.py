from src.main import *
from unittest.mock import patch

import pytest # type: ignore
import pytest_asyncio    # type: ignore

@pytest.mark.asyncio
async def teste_root():
   result = await  root()
   yield result
   assert result == {"message": "Hello World"}

@pytest.mark.asyncio
async def test_funcaoteste():
    with patch('random.randint', return_value=42):
        result = funcaoteste()
        yield result

    assert result == {"teste": True, "numero": 42}

@pytest.mark.asyncio
async def test_cadastrar_estudante():
    estudante_teste = Estudante(nome="João", idade="20", curso=True)
    result = create_estudante(estudante_teste) # type: ignore
    yield result
    assert estudante_teste == result

@pytest.mark.asyncio
async def update_estudante_positivo():
    result = update_estudante(10) # type: ignore
    yield result
    assert not result
   

@pytest.mark.asyncio
async def test_delete_estudante_negativo():
    result = update_estudante(-5) # type: ignore
    yield result
    assert not result

@pytest.mark.asyncio
async def test_delete_estudante_positivo():
    result = update_estudante(10) # type: ignore
    yield result
    assert not result
   


class Estudante(BaseModel):
    nome: str
    idade: str
    curso: bool