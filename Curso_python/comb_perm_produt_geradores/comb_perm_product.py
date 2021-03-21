"""
Combinations, Permutations e Product - Itertools
Combinação - Ordem não importa
Permutação - Ordem importa
Ambos não repetem valores únicos
Produto - Ordem importa e repete valores únicos
"""

from itertools import combinations, permutations, product

pessoas = ['Luiz', 'André', 'Eduardo', 'Letícia', 'Fabrício','Rose']

for grupo in combinations(pessoas,2):  # combinações 5 a 2 dos elementos da lista pessoas
    print(grupo)


# Combinações onde a ordem importa

for grupo in permutations(pessoas, 2):  # permutações 2 a 2 dos elementos da lista pessoas
    print(grupo)

for grupo in product(pessoas,repeat=2):  # ordem importe, repetindo valores.
    print(grupo)

#combinações 5 a 3 dos elementos da lista pessoas

for grupo in combinations(pessoas,3):
    print(grupo)