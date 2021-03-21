"""
Considerando duas listas de inteiros ou floats (lista A e lista B)
Some os valores nas listas retornando uma nova lista com os valores somados:

Se uma lista for maior que a outra, a soma só vai considerar o tamanho da menor.

Exemplo:
lista_a  = [1,2,3,4,5,6,7]
lista_b = [1,2,3,4]

###################### Resultado
lista_soma = [2,4,6,8]
"""

l1 = [1,2,3,4,5,6,7]
l2 = [1,2,3,4]

lc = list(zip(l1,l2))
l3 = [x + y for x, y in lc]
print(l3)

""" 
Solução do instrutor
 sem list comprehension
lista_a  = [1,2,3,4,5,6,7]
lista_b = [1,2,3,4]

lista_soma = []

for i in range(len(lista_b)):
    lista_soma.append(lista_a[i]+lista_b[i])
print(lista_soma)

com list comprehension
lista_soma = x + y for x, y in zip(lista_a,lista_b)]

"""