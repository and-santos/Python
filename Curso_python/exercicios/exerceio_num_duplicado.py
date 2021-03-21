"""
-> è uma lista de listas de números inteiros
-> As listas internas tem o tamanho de 10 elementos
-> As listas internas contém números entre 1 a 10 e eles podem ser duplicados

Exercício

-> Crie uma função que encontra o primeiro número duplicado na lista interna
    Requisitos:
        A ordem do número duplicado é considerada a partir da segunda ocorrência do número, ou seja, o número
        duplicado em si
        (o número duplicado em si).
        Exemplo: [1, 2, 3, ->3<-, 2, 1] 3
        Se não encontrar duplicados na lista, retorne -1

"""


lista_de_listas_de_inteiros = [
    [1,2,3,4,5,6,7,8,9,10],
    [9,1,8,9,9,7,2,1,6,8],
    [1,3,2,2,8,6,5,9,6,7],
    [3,8,2,8,6,7,7,3,1,9],
]

def encontra_primeiro_duplicado(param_lista_de_inteiros):
    numeros_checados = set()
    primeiro_duplicado = -1

    for numero in param_lista_de_inteiros:
        if numero in numeros_checados:
            primeiro_duplicado = numero
            break

        numeros_checados.add(numero)

    return primeiro_duplicado

for lista_de_inteiros in lista_de_listas_de_inteiros:
    print(lista_de_inteiros, encontra_primeiro_duplicado(lista_de_inteiros))