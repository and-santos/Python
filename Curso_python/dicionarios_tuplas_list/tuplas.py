"""
OBS: Tuplas não podem ser modificadas!
"""
t1 = (1,2,3,'a','Luiz Otávio')
t2 = 1, 2, 'a', 'b'  # para criar uma tupla não precisamos do parênteses explicitamente
t3 = 1,  # tupla de um elemento

t4 = t1 + t2  # concatenando tuplas
for v in t1:
    print(v)

print(t1[2])  # Fatiamento de tupla


n1, n2, n3, n4, *_ = t2  # desempacotando a tupla
print(n1)

# Também podemos repitir o valor da tupla utilizando o operador de multiplicação

t5 = (1,2,'Luiz',4,5)*20
print(t5)