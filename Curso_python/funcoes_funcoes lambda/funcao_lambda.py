# Função ou expressão lambda são funções anônimas

def funcao(arg,arg2):
    return arg * arg2

var = funcao(2,2)

# Podemos fazer o mesmo acima com a função lambda

a = lambda x, y: x * y

print(var)
print(a(2,2))

# Considere a lista abaixo

lista = [
    ['P1', 13],
    ['P2', 6],
    ['P3', 7],
    ['P4', 50],
    ['P5', 8]
]

def func(item):
    return item[1]

lista.sort(key=func) # do mais barato pro mais caro
lista.sort(key=func, reverse=True)  # do mais caro pro mais barato
lista.sort(key=lambda item: item[1])  # mesma coisa que  a linha 28, mas sem definir uma função
print(lista)
print(sorted(lista, key=lambda i: i[1]))  # outra maneira de imprimir preços, usando sorted()
print(sorted(lista, key=lambda i: i[1], reverse=True))