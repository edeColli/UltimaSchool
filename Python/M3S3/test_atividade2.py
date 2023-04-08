import pytest
from atividade2 import calcular_total_conta

menu = {"HotDog": 100, "DoubleHotDog": 101, "X-Egg": 102, "X": 103,
        "X-Bacon": 104, "X-Tudo": 105, "Refri": 200, "IceTea": 201}


def test_pedir_cachorro_quente():
    assert calcular_total_conta(menu.get("HotDog")) == 9.0


def test_pedir_cachorro_quente_duplo():
    assert calcular_total_conta(menu.get("DoubleHotDog")) == 11.0


def test_pedir_x_egg():
    assert calcular_total_conta(menu.get("X-Egg")) == 12.0


def test_pedir_x_salada():
    assert calcular_total_conta(menu.get("X")) == 12.0


def test_pedir_x_bacon():
    assert calcular_total_conta(menu.get("X-Bacon")) == 14.0


def test_pedir_x_tudo():
    assert calcular_total_conta(menu.get("X-Tudo")) == 17.0


def test_pedir_refri_lata():
    assert calcular_total_conta(menu.get("Refri")) == 5.0


def test_pedir_cha_gelado():
    assert calcular_total_conta(menu.get("IceTea")) == 4.0


def test_pedir_cachorro_quente_mais_refri():
    total = calcular_total_conta(menu.get("HotDog"))
    total += calcular_total_conta(menu.get("Refri"))
    assert total == 14.0


def test_pedir_menu_completo():
    total = 0
    for value in menu.values():
        total += calcular_total_conta(value)
    assert total == 84.0


def test_pedir_x_tudo_e_cha_gelado():
    total = calcular_total_conta(menu.get("X-Tudo"))
    total += calcular_total_conta(menu.get("IceTea"))
    assert total == 21.0


def test_opcao_invalida():
    assert calcular_total_conta(menu.get("Nada")) == -1.0
