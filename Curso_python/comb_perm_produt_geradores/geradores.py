"""
Geradores, Iteradores e Iteráveis em python
Uma lista é um objeto iterável
para confirmar, podemos utilizar o comando
hasattr(lista, '__iter__'). Para um objeto iterável deve retornar o booleano "True".
String também é um objeto iterável,
Números no entanto NÃO SÃO OBJETOS ITERÁVEIS

Se for um objeto iterável, podemos utiliza-lo dentro de um loop "for" .
"""

lista = [0,1,2,3,4,5]

print(hasattr(lista, '__iter__'))

for v in lista:
    print(v)

print(hasattr(lista, '__next__')) # Retorna falso se não for um iterador

#tornando a lista em iterador

lista = iter(lista)
#lista = __iter__    #método alternativo

print(next(lista))
print(next(lista))
print(next(lista))
print(next(lista))

# Gerador
# Geradores podem ser utilizados para otimização de memória
lista = list(range(1000))
import sys
print(sys.getsizeof(lista)) #tamanho em bytes ocupado pelo elemento

import time
def gera():
    r = []
    for n in range(100):
        yield n
        time.sleep(0.1)
    return r

g = gera()

"""
for v in g:
    print(v)
"""

print(hasattr(g,'__iter__'))  # Verifica se o objeto é iterável
print(hasattr(g, '__next__')) # Verifica se o objeto é um iterador

"""
def gera():
    variavel = 'Valor 1'
    yield variavel
    variavel = 'Valor 2'
    yield variavel
    variavel = 'Valor 3'
    yield variavel
"""

l1 = [x for x in range(100000)]
print(type(lista))
l2 = (x for x in range(100000))  # Gerador
print(type(l2))

print(sys.getsizeof(l1))
print(sys.getsizeof(l2))

# Obes