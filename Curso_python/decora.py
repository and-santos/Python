"""
def fala_oi():
    print('Oi')


variavel = fala_oi

print(type(variavel))
"""

def master(funcao):
    def slave(*args,**Kwargs):
        print('Agora estou decorada')
        funcao(*args,**Kwargs)
    return slave

@master
def fala_oi():
    print('Oi')


def outra_funcao(msg):
    print(msg)
    
outra_funcao('Olá, eu sou Andre')

# Exemplo

from time import time
from time import sleep


def velocidade(funcao):
    def interna(*args,**kwargs):
        start_time = time()
        resultado = funcao(*args,**kwargs)
        end_time = time()
        tempo = (end_time - start_time) * 1000
        print(f'\n A função {funcao.__name__} levou {tempo:.2f}ms para executar.')
        return resultado
    return interna

@velocidade
def demora():
    for i in range(1000):
        print(i,end='')

demora()