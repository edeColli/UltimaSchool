import pytest
from atividade3 import calcular_frete
from atividade3 import calcular_multiplicador_peso
from atividade3 import calcular_multiplicador_rota
from atividade3 import calcular_preco_volume
from atividade3 import get_volume
from atividade3 import validar_medida
from atividade3 import get_peso


def test_validar_medida_invalida():
    assert validar_medida("abc") == -1


def test_validar_medida_valida():
    assert validar_medida(10) == 10


def test_validar_volume_valido():
    altura = validar_medida(10)
    largura = validar_medida(10)
    comprimento = validar_medida(10)
    assert get_volume(altura, largura, comprimento) == 1000


def test_peso_valido():
    assert get_peso(25) == 25.0


def test_peso_invalido():
    assert get_peso(31) == -1


def test_validar_volume_invalido():
    altura = validar_medida(150)
    largura = validar_medida(150)
    comprimento = validar_medida(150)
    assert get_volume(altura, largura, comprimento) == -1


def test_validar_preco_volume_menor_1000():
    assert calcular_preco_volume(900) == 10.0


def test_validar_preco_volume_maiorigual_1000_e_menor_10000():
    assert calcular_preco_volume(1500) == 20.0


def test_validar_preco_volume_maiorigual_10000_e_menor_30000():
    assert calcular_preco_volume(10500) == 30.0


def test_validar_preco_volume_maiorigual_30000_e_menor_100000():
    assert calcular_preco_volume(45000) == 20.0


def test_calcular_multiplicador_peso_em_gramas():
    assert calcular_multiplicador_peso(0.05) == 1


def test_calcular_multiplicador_peso_ate_1kg():
    assert calcular_multiplicador_peso(0.950) == 1.5


def test_calcular_multiplicador_peso_ate_10kg():
    assert calcular_multiplicador_peso(5.8) == 2.0


def test_calcular_multiplicador_peso_ate_30kg():
    assert calcular_multiplicador_peso(15) == 3.0


def test_calcular_multiplicador_peso_invalido_acima30k():
    assert calcular_multiplicador_peso(31) == 0


def test_calcular_multiplicado_rota_sr():
    assert calcular_multiplicador_rota('sr') == 1.0


def test_calcular_multiplicado_rota_rs():
    assert calcular_multiplicador_rota('rs') == 1.0


def test_calcular_multiplicado_rota_bs():
    assert calcular_multiplicador_rota('bs') == 1.2


def test_calcular_multiplicado_rota_sb():
    assert calcular_multiplicador_rota('sb') == 1.2


def test_calcular_multiplicado_rota_br():
    assert calcular_multiplicador_rota('br') == 1.5


def test_calcular_multiplicado_rota_rb():
    assert calcular_multiplicador_rota('rb') == 1.5


def test_calcular_multiplicado_rota_invalida():
    assert calcular_multiplicador_rota('') == 0.0


def test_calcular_frete_volume400_3kg_rio_brasilia():
    volume = get_volume(5, 8, 10)
    preco_volume = calcular_preco_volume(volume)
    multiplicador_peso = calcular_multiplicador_peso(3.0)
    multiplicador_rota = calcular_multiplicador_rota("rb")
    assert calcular_frete(preco_volume, multiplicador_peso,
                          multiplicador_rota) == 30.0


def test_calcular_frete_volume_200_500GR_Rio_SP():
    volume = get_volume(5, 5, 8)
    preco_volume = calcular_preco_volume(volume)
    multiplicador_peso = calcular_multiplicador_peso(0.5)
    multiplicador_rota = calcular_multiplicador_rota("rs")
    assert calcular_frete(preco_volume, multiplicador_peso,
                          multiplicador_rota) == 15.0


def test_calcular_frete_5GR():
    volume = get_volume(5, 5, 8)
    preco_volume = calcular_preco_volume(volume)
    multiplicador_peso = calcular_multiplicador_peso(0.05)
    multiplicador_rota = calcular_multiplicador_rota("rs")
    assert calcular_frete(preco_volume, multiplicador_peso,
                          multiplicador_rota) == 10.0


def test_calcular_frete_500GR():
    volume = get_volume(5, 5, 8)
    preco_volume = calcular_preco_volume(volume)
    multiplicador_peso = calcular_multiplicador_peso(0.5)
    multiplicador_rota = calcular_multiplicador_rota("rs")
    assert calcular_frete(preco_volume, multiplicador_peso,
                          multiplicador_rota) == 15.0


def test_calcular_frete_3kg():
    volume = get_volume(5, 5, 8)
    preco_volume = calcular_preco_volume(volume)
    multiplicador_peso = calcular_multiplicador_peso(3.0)
    multiplicador_rota = calcular_multiplicador_rota("rs")
    assert calcular_frete(preco_volume, multiplicador_peso,
                          multiplicador_rota) == 20.0


def test_calcular_frete_15kg():
    volume = get_volume(5, 5, 8)
    preco_volume = calcular_preco_volume(volume)
    multiplicador_peso = calcular_multiplicador_peso(15.0)
    multiplicador_rota = calcular_multiplicador_rota("rs")
    assert calcular_frete(preco_volume, multiplicador_peso,
                          multiplicador_rota) == 30.0


def test_calcular_frete_45kg():
    volume = get_volume(5, 5, 8)
    preco_volume = calcular_preco_volume(volume)
    multiplicador_peso = calcular_multiplicador_peso(45.0)
    multiplicador_rota = calcular_multiplicador_rota("rs")
    assert calcular_frete(preco_volume, multiplicador_peso,
                          multiplicador_rota) == 0.0


def test_calcular_frete_volume500():
    volume = get_volume(2, 5, 50)
    preco_volume = calcular_preco_volume(volume)
    multiplicador_peso = calcular_multiplicador_peso(1.0)
    multiplicador_rota = calcular_multiplicador_rota("rs")
    assert calcular_frete(preco_volume, multiplicador_peso,
                          multiplicador_rota) == 20.0


def test_calcular_frete_volume1500():
    volume = get_volume(30, 25, 2)
    preco_volume = calcular_preco_volume(volume)
    multiplicador_peso = calcular_multiplicador_peso(1.0)
    multiplicador_rota = calcular_multiplicador_rota("rs")
    assert calcular_frete(preco_volume, multiplicador_peso,
                          multiplicador_rota) == 40.0


def test_calcular_frete_volume15000():
    volume = get_volume(30, 25, 20)
    preco_volume = calcular_preco_volume(volume)
    multiplicador_peso = calcular_multiplicador_peso(1.0)
    multiplicador_rota = calcular_multiplicador_rota("rs")
    assert calcular_frete(preco_volume, multiplicador_peso,
                          multiplicador_rota) == 60.0


def test_calcular_frete_volume64000():
    volume = get_volume(40, 40, 40)
    preco_volume = calcular_preco_volume(volume)
    multiplicador_peso = calcular_multiplicador_peso(1.0)
    multiplicador_rota = calcular_multiplicador_rota("rs")
    assert calcular_frete(preco_volume, multiplicador_peso,
                          multiplicador_rota) == 40.0


def test_calcular_frete_volume150000():
    volume = get_volume(10, 100, 150)
    preco_volume = calcular_preco_volume(volume)
    multiplicador_peso = calcular_multiplicador_peso(1.0)
    multiplicador_rota = calcular_multiplicador_rota("rs")
    assert calcular_frete(preco_volume, multiplicador_peso,
                          multiplicador_rota) == 20.0


def test_calcular_frete_rota_Brasilia_Rio():
    volume = get_volume(5, 5, 5)
    preco_volume = calcular_preco_volume(volume)
    multiplicador_peso = calcular_multiplicador_peso(0.5)
    multiplicador_rota = calcular_multiplicador_rota("br")
    assert calcular_frete(preco_volume, multiplicador_peso,
                          multiplicador_rota) == 22.5


def test_calcular_frete_rota_Brasilia_SP():
    volume = get_volume(5, 5, 5)
    preco_volume = calcular_preco_volume(volume)
    multiplicador_peso = calcular_multiplicador_peso(0.5)
    multiplicador_rota = calcular_multiplicador_rota("bs")
    assert calcular_frete(preco_volume, multiplicador_peso,
                          multiplicador_rota) == 18.0


def test_calcular_frete_rota_Rio_Brasilia():
    volume = get_volume(5, 5, 5)
    preco_volume = calcular_preco_volume(volume)
    multiplicador_peso = calcular_multiplicador_peso(0.5)
    multiplicador_rota = calcular_multiplicador_rota("rb")
    assert calcular_frete(preco_volume, multiplicador_peso,
                          multiplicador_rota) == 22.5


def test_calcular_frete_rota_Rio_SP():
    volume = get_volume(5, 5, 5)
    preco_volume = calcular_preco_volume(volume)
    multiplicador_peso = calcular_multiplicador_peso(0.5)
    multiplicador_rota = calcular_multiplicador_rota("rs")
    assert calcular_frete(preco_volume, multiplicador_peso,
                          multiplicador_rota) == 15.0


def test_calcular_frete_rota_SP_Rio():
    volume = get_volume(5, 5, 5)
    preco_volume = calcular_preco_volume(volume)
    multiplicador_peso = calcular_multiplicador_peso(0.5)
    multiplicador_rota = calcular_multiplicador_rota("sr")
    assert calcular_frete(preco_volume, multiplicador_peso,
                          multiplicador_rota) == 15.0


def test_calcular_frete_rota_SP_Brasilia():
    volume = get_volume(5, 5, 5)
    preco_volume = calcular_preco_volume(volume)
    multiplicador_peso = calcular_multiplicador_peso(0.5)
    multiplicador_rota = calcular_multiplicador_rota("sb")
    assert calcular_frete(preco_volume, multiplicador_peso,
                          multiplicador_rota) == 18.0
