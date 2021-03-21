"""
Dicionário é uma estrutura de dados que possue um par de dados (chave,valor)
Para chaves, podemos utilizar qualqur valor imutável em python. (str,tuplas,números)
"""


d1 = {'chave1': 'valor da chave'}
#d1 = dict(chav1='Valor da chave', chave2='Valor da outra chave')  # Outra maneira de criar uma chave
d1['nova_chave'] = 'Valor da nova chave'  # Criando uma nova chave

print(d1)
print(d1['chave1'])

# d1 = {'chave': 'valor','chave':}  # Ao duplicar chaves, ela adquire o último valor informado

d1.update( {'nova_chave2':'novo_valor3'} )  # Método alternativo para riar uma nova chave

del d1['chave1']  # Apagando uma chave no dicionário

print(d1)
print('nova_chave' in d1)  # Retorna True se 'nova_chave' existe em d1, False caso contrário
print('valor' in d1.values())  # Reetorna True se 'valor' existe nos valores do dict, False caso contrário
print(len(d1))  # Tamanho do dicionário

# Iterando sobre um dicionário

for k in d1:
    print(k)

# Acssando os valores no loop

for k in d1.values():
    print(k)

# Acessando chave e valor ao mesmo tempo
for k in d1.items():
    print(k)

# Aceessando chave e valor separadamente desempacotados
for k, v in d1.items():
    print(k, v)

clientes = {
    'cliente1' : {
        'nome' : 'Luiz',
        'sobrenome' : 'Otávio',
    },
    'cliente2' : {
        'nome' : ' JOão',
        'sobrenome' : 'Moreira',
    },
} 

for clientes_k, clientes_v in clientes.items():
    print(f'Exibindo {clientes_k}')
    for dados_k, dados_v in clientes_v.items():
        print(f'\t{dados_k} = {dados_v}')

"""
d1 = {1: 'a', 2: 'b', 3: 'c'}
v = d1

v[1] = 'Luiz'
print(d1)
print(v)
Em python, devemos ficar atentos que v = d1 não gera um novo dicionário, isto é 
ambos apontam para o mesmo valor ocupado na memória
print(v == d1) resulta em True, mostrando que de fato são iguais.

Para fazer uma shell copy de um dicionário, podemos fazer

v = d1.copy()

"""
# Convertendo uma lista em dicionário, Devem seguir a estrutura abaixo.
#Também serve para tuplas que segue a mesma estrutura.

lista = [
    ['c1', 1],
    ['c2', 2],
    ['c3', 3],
]

d1 = dict(lista)
print(d1)

# Eliminando a última chave de um dicionário

d1 = {
    1: 2,
    2: 3,
    4: 5,
}

d1.pop(4)

# Para eliminar o último item do dicionário:
d1.popitem()
print(d1)

# Concatenando dicionários

d2 = {
    'a' : 'b',
    'c' : 'd',
}

d1.update(d2)