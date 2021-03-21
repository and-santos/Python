# listas, tuplas, strings --> Sequências -> Iteravel

"""
Iteradores e gerados são utilizados para serem consumidos, após o fim da sequência,
é como eles estivessem "esgotados" não podendo mais ser utilizados
"""
nome = 'Luiz Otavio' 

iterador = iter(nome)
gerador = (letra for letra in nome)

print(next(gerador))
print(next(gerador))
print(next(gerador))
print(next(gerador))

print('OLHA O FOR')

for letra in gerador:
    print(letra)

print('OLHA O OUTRO FOR')

for letra in gerador:
    print(letra)

"""
print(next(iterador))
print(next(iterador))
print(next(iterador))
print(next(iterador))
print(next(iterador))
print(next(iterador))
print(next(iterador))
print(next(iterador))
print(next(iterador))
print(next(iterador))
print(next(iterador))
"""


for letra in nome:
    print(letra)

    print ('#'*80)

    for letra in nome:
        print(letra)

    print(nome)