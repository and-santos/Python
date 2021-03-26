"""
04.252.011/0001-10 -> válido 40.668.134/0001-61 -> não é valido 71.506.168/0001-11 -> válido
12.544.992/0001-05 -> não é valido

0   4   2   5   2   0   1   1   0   0   0   1   X   X
5   4   3   2   9   8   7   6   5   4   3   2
0   16  6   10  18  0   7   6   0   0   0   2 = 65 ##
Fórmula -> 11 - (65 % 11) = 1
Primeiro digito = 1

0   4   2   5   2   0   1   1   0   0   0   1   1   X
6   5   4   3   2   9   8   7   6   5   4   3   2
0   20  8   15  4   0   8   7   0   0   0   3   2 = 67 ##
Fórmula -> 11 - (67 % 11) = 11 (como o resultado é maior que 9, então é 0)
Segundo digito = 0

Novo CNPJ + Digitos = 04.252.011/0001-10
CNPJ Original =       04.252.011/0001-10
Válido

Recap
543298765432 -> Primeiro digito
"""

#Formula = 11 - (digito % 11) = 1

cnpj = input('Insira um CNPJ: ')
cnpj = cnpj.replace('.','')
cnpj = cnpj.replace('/','')
cnpj = cnpj.replace('-','')
cnpj_para_teste = list(cnpj)
cnpj_teste = list(cnpj[:12])
novo_cnpj = cnpj

cont1 = 5
cont2 = 9
size = len(cnpj_teste)
multiplicador = []

for i in range(size):
    multiplicador.append(cont1 - i)
    if cont1 - i == 2:
        break

for j in range(size):
    multiplicador.append(cont2 - j)
    if len(multiplicador) == size:
        break

result = [x * int(y) for x,y in list(zip(multiplicador,cnpj_teste))]

soma_result = sum(result)

Formula = 11 - (soma_result % 11)
if Formula > 9:
    Formula = 0
cnpj_teste.append(str(Formula))

# Parte 2

cont1 = 6
cont2 = 9
size = len(cnpj_teste)
multiplicador = []

for i in range(size):
    multiplicador.append(cont1 - i)
    if cont1 - i == 2:
        break

for j in range(size):
    multiplicador.append(cont2 - j)
    if len(multiplicador) == size:
        break

result = [x * int(y) for x,y in list(zip(multiplicador,cnpj_teste))]



soma_result = sum(result)

Formula = 11 - (soma_result % 11)
if Formula > 9:
    Formula = 0

cnpj_teste.append(str(Formula))

if cnpj_teste == cnpj_para_teste:
    print('CNPJ Válido. ')
else:
    print('Este CNPJ não é válido. ')
