# add (adiciona), update (atualiza), clear, discard
# union | (une)
# intersection & (todos os elementos presentes nos dois sets)
#difference - (ellementos apenas no set da esquerda)
#symmetric_difference - (Elementos que estão nos dois sets, mas não em ambos)

s1 = {1,2,3,4,5,6}  # suportam apenas elemenetos imutáveis

# print(s1)

# Podemos interar sobre o set:
"""
for v in s1:
    print(v)
"""
# Um set vazio deve ser criado da seguinte forma
s1 = set()
# Adicionando elementos
s1.add(1)
s1.add(2)
s1.add(3)

# Função update
s1 = set()
s1.update('Python')  # Adiciona elmentos ao conjunto, iterando sobre a palbra Python.

s1.update([1,2,3,4,5], {5,6,7,8})

# Geralmente usamos set para remover elementos duplicados de uma lista

l1 = [1,2,1,1,3,4,5,6,6,6,6,6,6,7,8,9,'Luiz','Luiz']
l1 = set(l1)
l1 = list(l1)

s1 = {1,2,3,4,5,7}
s2 = {1,2,3,4,5,6}

s3 = s1 | s2  # união
print(s3)

s3 = s1 & s2  # interseção
print(s3)

s3 = s1 - s2 # pega os elementos de s1 e que não estam presentes em s2
print(s3)

s3 = s2 ^ s1 # o resultado de saída são os elementos de s1 que não estão em s2 e vice versa.
print(s3)

l1 = ['Luiz','João', 'Maria']
l2 = ['João', 'Maria','Maria','Luiz','Luiz','Luiz','Luiz','Luiz' ]

l1 = list(set(l1))
l2 = list(set(l2))

if l1 == l2:
    print('l1 é igual a l2')
else:
    print('l1 é diferente de l2')