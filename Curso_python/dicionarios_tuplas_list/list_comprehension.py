"""
List comprehension - Compreensão de lista:
    É uma construção sintática de programação para criação de uma lista
    baseada em listas existentes.
Usadas para otimização, e diminuir a quantidade de linhas de código
"""

l1 = [1,2,3,4,5,6,7,8,9]
#print(l1)
ex1 = [ variavel for variavel in l1]
#print(ex1)
ex2 = [v*2 for v in l1]
#print(ex2)
ex3 = [ (v,v2) for v in l1 for v2 in range(3)]
#print(ex3)



l2 = ['Luiz', 'Mauro', 'Maria']
#print(l2)
ex4 = [v.replace('a','@') for v in l2]
#print(ex4)

tupla = (
    ('chave','valor'), 
    ('chave2','valor2')
)

#print(tupla)

ex5 = [(x,y) for x,y in tupla]
#print(ex5)

# inversão
ex6 = [(y,x) for x, y in tupla]
#print(ex6)

l3 = list(range(100))
ex7 = [v for v in l3 if  v % 3 == 0 if v % 8 == 0]
# pegamos todos os números de l3 divisíveis por 3 e 8
#print(ex7)

ex8 = [v if v % 3 == 0 and v % 8 == 0 else 0 for v in l3]
print(ex8)
