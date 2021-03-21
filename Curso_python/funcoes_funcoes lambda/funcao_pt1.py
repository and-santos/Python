"""
Funções - def em Python (Parte 1)
"""
def saudacao(msg='Olá', nome='usuário'):
    nome = nome.replace('e','3')
    msg = msg.replace('e','3')
    print(msg, nome)
    
saudacao(nome='Zezinho',msg = 'Hi')
saudacao('Zeinho', 'Hi')
saudacao('Olá', 'André')
saudacao('Olá', 'André')
saudacao('Olá', 'André')
