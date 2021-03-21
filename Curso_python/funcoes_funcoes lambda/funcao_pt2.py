"""
Funções - def em Python (Parte 1)
"""


def divisao(n1, n2):
    if n2 == 0:
        return

    return n1 / n2

divide = divisao(8,0)

if divide:
    print(divide)
else:
    print('Conta inválida')

def dumb():
    return True

var = dumb()

print(var, type(var))

"""
def f(var):
    print(var)

def dumb():
    return f

var = dumb()
print(id(var), id(f))

Neste caso, temos que var é equivalente a função f.
Uma função pode retornar qualquer coisa em python, incluindo outra função
"""