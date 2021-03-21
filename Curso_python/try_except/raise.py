# https://docs.python.org/3/library/exceptions.html -> Todas as exceções que ocorrem em python


"""
def divide(n1, n2):
    try:
        return n1 / n2
    except ZeroDivisionError as error:
        print('Log: ', error)
        raise


try:
    print(divide(2,0))
except ZeroDivisionError as error:
    print(error)
"""

def divide(n1, n2):
    if n2 == 0:
        raise ValueError("n2 não pode ser 0.")
    return n1 / n2

try:
    print(divide(n1=2,n2=0))
except ValueError as error:
    print('Você está tentando dividir por 0.')
    print('Log:', error)
    # print(error) 