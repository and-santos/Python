"""
1 - Crie uma função que exibe uma saudação com os parâmetros saudacao e nome.

2- Crie uma função que recebe 3 números como parâmetros e exiba a soma entre eles.

3 - Crie uma função que receba 2 números. O primeiro é um valor e o segundo um percentual (ex. 10%).
Retorne (return) o valor do primeiro número somado do aumento do percentual do mesmo

4 - Fizz Buzz - Se o parâmetro da função for divisível por 3, retorne fizz, se o parâmetro da função
for divisível por 5, retone buzz. Se o parâmetro da função for divisível por 5 e por 3, retorne
FizzBuzz, caso contrário, retorne o número enviado.
"""

# Exercício 1
def saudacao(msg='Olá',nome='usuário'):
    print(msg,nome)

# Exercício 2
def soma(n1,n2,n3):
    sum = n1 + n2 + n3
    print(sum)

# Exercício 3
def percentual(val,per):
    porcentagem = (val/100)*per
    return val + porcentagem

# Exercício 4
def fizzbuzz(num):
    if num % 3 == 0 and num % 5 == 0:
        return 'FizzBuzz'
    elif num % 3 == 0:
        return 'Fizz'
    elif num % 5 == 0:
        return'Buzz'
    else:
         return num


print(fizzbuzz(7))

"""
# Exercício 1
Soluções do instrutor
def saudacao(sqaudacao, nome):
    print(f'{saudacao} {nome}')

# Exercício 2
def soma(n1, n2, n3):
    print(n1 + n2 + n3)

# Exercício 3
def aumento_percentual(valor, percentual):
    return valor + (valor * percentual / 100)

# Exercícios FizzBuzz
def fb(n):
    if num % 3 == 0 and num % 5 == 0:
        return 'FizzBuzz'
    if num % 3 == 0:
        return 'Fizz'
    ff num % 5 == 0:
        return 'Buzz'
    return n
"""