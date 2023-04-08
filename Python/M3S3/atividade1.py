def calcular_desconto(quantidade: int, valor_unitario: float) -> tuple:
    if valor_unitario < 0 or quantidade < 0:
        raise ValueError(
            "Valor unitário e quantidade devem ser maiores que zero")

    desconto = 1

    if quantidade >= 10 and quantidade <= 99:
        desconto = 0.95
    elif quantidade >= 100 and quantidade <= 999:
        desconto = 0.90
    elif quantidade >= 1000:
        desconto = 0.85

    # No desconto o completo de até 1 é o valor do desconto.
    # Ex: 0,85 tem 15% de desconto. -> 1 - 0,85 = 0.15

    valor_com_desconto = valor_unitario * desconto * quantidade
    valor_sem_desconto = valor_unitario * quantidade

    return valor_sem_desconto, valor_com_desconto


if __name__ == '__main__':
    quantidade = int(input('Quantidade: '))
    valor_unitario = float(input('Valor unitário do produto: '))
    valor_sem_desconto, valor_com_desconto = calcular_desconto(
        quantidade, valor_unitario)
    print(f'Valor total sem desconto: {valor_sem_desconto:.2f} R$')
    print(f'Valor total com desconto: {valor_com_desconto:.2f} R$')
