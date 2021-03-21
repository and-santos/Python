"""
funções (def) em PYthon -*args **kwargs -
arg = argumeento - convenções
kwargs - keyword arguments - convnções
"""
# A partir do momento que defino um argumento default, os proximos também precisam ser default
# o argumento da chamada dev eser nomeada após a declaração default

def func(*args,**kwargs):
    print(args)
    print(kwargs)

    idade = kwargs.get('idade')  # Usado para vreificar see uma variavl tem valor nulo ou não.

    if idade is not None:
        print(idade)

lista = [1,2,3,4,5]
lista2 = [10,20,30,40,50]

func(1,2,3,4,5)  #argumentos empacotados em uma tupla. Em tuplas, não podemos alteerar o itm de uma tupla

func(*lista, *lista2,nome='Luiz', sobrenome='Miranda',idade=30)  # Print lista desempacotada dentro d uma tupla

func(lista,10,20,30,40,50)  # PRint lista dentro da tupla. A lista é retirada em um índicee da dupla

