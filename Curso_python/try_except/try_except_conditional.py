# https://docs.python.org/3/library/exceptions.html -> Todas as exceções que ocorrem em python

def converte_numero(valor):
    try:
        valor = int(valor)
        return valor
    except ValueError:
        try:
            valor = float(valor)
            return valor
        except ValueError:
            pass



while True:
    numero = converte_numero(input('Digite um número: '))

    if numero is None:
        print('Erro> isso não é um número')
    else:
        print(numero * 2)

