# https://docs.python.org/3/library/functions.html#open -> Referência

# Como criar, ler escrever e apagar arquivos

"""

# Abrindo arquivos
file = open('abc.txt','w+')  # abre um arquivo no modo escrita e leitura
file.write('Linha 1\n')
file.write('Linha 2\n')
file.write('Linha 3\n')

file.seek(0, 0)  #retorna ao início do arquivo
print('Lendo linhas: ')
print(file.read())

print('########')
file.seek(0,0)
print(file.readline(),end='')  #Le o arquivo linha por linha
print(file.readline(),end='')
print(file.readline(),end='')
print('########')

file.seek(0,0)
for linha in file.readlines():
    print(linha,end='')

file.close()
"""

with open('abc.txt', 'a+') as file:  # a+ edita sem apagar o que estiver dentro do arquivo
    file.write('Outra linha \n')
    file.seek(0)
    print(file.read())


# Apagando arquivo
import os
os.remove('abc.txt')

# Criando um arquivo .json a partir de dict
import json

d1 = {
    'Pessoa 1': {
        'nome': 'Luiz',
        'idade': 25,
    },
    'Pessoa 2': {
        'nome': 'Rose',
        'idade': 30,
    },
}

print(d1)

d1_json = json.dumps(d1, indent=True)

with open('abc.json','w+') as file:
    file.write(d1_json)
print(d1_json)