from dados import produtos, pessoas, lista
from functools import reduce

"""
Exemplo acumulador
acumula = 0
for item in lista:
    acumula += item

print(acumula)
"""


# Usamos reduce como uma forma mais sucinta de acunulador
soma_lista = reduce(lambda ac, i: i + ac, lista, 0)
print(soma_lista)

soma_precos = reduce(lambda ac, p: p['preco'] + ac, produtos, 0)
print(soma_precos / len(produtos))

soma_idades = reduce(lambda ac, p: ac + p['idade'],pessoas, 0)
print(soma_idades / len(pessoas))
