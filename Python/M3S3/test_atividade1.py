import pytest
from atividade1 import calcular_desconto


def test_desconto_10_a_99():
    assert calcular_desconto(10, 10.0) == (100.0, 95.0)


def test_desconto_100_a_999():
    assert calcular_desconto(100, 10.0) == (1000.0, 900.0)


def test_desconto_acima_1000():
    assert calcular_desconto(1001, 10.0) == (10010.0, 8508.5)


def test_sem_desconto():
    assert calcular_desconto(9, 10.0) == (90.0, 90.0)


def test_valor_unitario_negativo():
    with pytest.raises(ValueError):
        calcular_desconto(10, -10.0)


def test_quantidade_negativa():
    with pytest.raises(ValueError):
        calcular_desconto(-10, 10.0)
