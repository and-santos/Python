
variavel = 'valor'  # variavel em escopo global. Pode ser acessada por qualquer local da aplicação.

def func():
    print(variavel)


# Variaveis alteradas dentro de funções são acessiveeis localmente. Neste caso apenas dentro da função
# Neste caso temos uma variável local 
# Mudar uma variavel global dentro de uma função náo é uma boa pratica de programação
def func2():
    #global variavel
    variavel = 'Outro valor'  
    print(variavel)

func()
func2()

"""
def func3():
    print(variavel)
    variavel = 1234
    print(variavel)

A funcao func3 gera o erro: UnboundLocalError: local variable 'variavel' referenced before assignment
pois a variavel é tratada como local, mesmo que tenha o mesmo nome da variavel global definida
anteriormente.
"""