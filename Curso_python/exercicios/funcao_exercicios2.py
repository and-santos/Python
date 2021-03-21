"""
1 - Crie uma função1 que recebe uma função2 como parâmetro e retorne o valor da função2 executada

2 - Crie uma função1 que recebe uma função2 como parâmetro e retorne o valor da função2 executada. Faça a
função1 executar duas funções que recebam um número diferente de argumentos
"""

# Exercício 1
def func2(nome):
    return f'Olá {nome}'


def func1(nome):
    print(nome)

func1(func2('André'))


# Exercício 2
def func3(nome,sobrenome):
    print(nome,sobrenome)

func3(func2('André'),'Santos')

"""
Soluções do Instrutor

# Exercício 1
def ola_mundo():
    return 'Olá mundo!'

def mestre(funcao):
    return funcao()

executando = mestre(ola_mundo)
print(executando)

# Exercício 2
def mestre(funcao, *args, **kwargs):
    return funcao(*args,**kwargs)

def fala_oi(nome):
    return f'Oi {nome}'

def saudacao(nome,saudacao):
    return f'{saudacao} {nome}'

executando = mestre(fala_oi,'Luiz')
executando2 = mestre(saudacao, 'Luiz','saudacao='Bom dia!')

print(executando)
print(executando2)
"""