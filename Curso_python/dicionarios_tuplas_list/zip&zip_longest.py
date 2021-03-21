"""
Zip - Unindo iteráveis
Zip_longest - Itertools
"""

from itertools import zip_longest, count
### Código

## Parte 1 ## -- zip

cidades = ['São Paulo', 'Belo Horizonte', 'Salvador', 'Monte Belo']
estados = ['SP','MG','BA']

cidades_estados = zip(cidades,estados)

for valor in cidades_estados:
    print(valor)



# Podemos fazer um dict com as listas unidas: dict(cidades_estados))
# o zip uni até o tamanho da menor lista

## Parte 2 ## -- zip_longest

indice = count()
cidades = ['São Paulo', 'Belo Horizonte', 'Salvador', 'Monte Belo']
estados = ['SP','MG','BA']

cidades_estados = zip(
    indice,
    estados,
    cidades
    #fillvalue='Estado'
     )

for valor in cidades_estados:
    print(valor)

   
for indice, estado, cidade in cidades_estados:
    print(indice, estado, cidade)
