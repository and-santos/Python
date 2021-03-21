"""
count- Itertools (iterador)
"""

from itertools import count

contador = count(start=5,step=-1)  # Contador infinito


for valor in contador:
    print(round(valor,2))

    if valor >= 10 or valor <= -10:
        break


contador = count()
lista = ['Luiz','João','Maria']
lista = zip(contador,lista)
print(list(lista))