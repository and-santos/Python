string = '01234567890123456789012345678901234567890123456789'

"""
lista = ['0123456789','0123456789','0123456789','0123456789','0123456789']

retorno = '0123456789.0123456789.0123456789.0123456789.0123456789'
"""

lista = [string[0:10] for v in range(5)] #adiciona todos os elementos
print(lista)


string = lista[0] + '.' + lista[1] + '.' + lista[2] + '.' + lista[3] + '.' + lista[4] + '.' 
print(string)

# Funciona.. mas poderia ser melhor

"""
Solução do Instrutor
string = '01234567890123456789012345678901234567890123456789'

n = 10
lista = [string[(i:i+n) for i in range(0,len(string), n)]
retorno = '.'.join(lista)
print(lista)
print(retorno)



"""