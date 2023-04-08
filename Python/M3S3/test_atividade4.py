
import pytest
import functools
from atividade4 import pecas
from atividade4 import imprimir_peca
from atividade4 import gerar_codigo
from atividade4 import insert_peca
from atividade4 import excluir_peca


def cadastrar_peca(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        insert_peca(1, 'Tubo 25 mm', 'Tigre', 5.00)
        assert len(pecas) > 0
        return func(*args, **kwargs)
    return wrapper


def test_gerar_codigo_valido():
    assert gerar_codigo() == len(pecas)+1


@cadastrar_peca
def test_cadastrar_peca():
    assert len(pecas) > 0


@cadastrar_peca
def test_remover_peca():
    assert excluir_peca(1) == True


def test_remover_peca_inexistente():
    assert excluir_peca(10) == False


@cadastrar_peca
def test_imprimir_peca(capsys):
    imprimir_peca(pecas[0])
    # captura a saida do print no terminal
    captured = capsys.readouterr()
    assert captured.out == """Código: 001\nFabricante: Tigre\nValor: 5.00 R$\n"""
