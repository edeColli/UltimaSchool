def decorator_imprimir(func):
    def wrapper(*args, **kargs):
        result = func(*args, **kargs)
        capital, taxa, tempo = args
        print(f"CAPITAL: {capital} TAXA: {taxa} TEMPO: {tempo}")
        print(f"RESULADO: {result}")
    return wrapper


@decorator_imprimir
def juros_simples(capital, taxa, tempo):
    return capital * (taxa / 100) * tempo


juros_simples(1000, 5, 6)
