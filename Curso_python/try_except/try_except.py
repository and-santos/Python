# https://docs.python.org/3/library/exceptions.html -> Todas as exceções que ocorrem em python

try:
    a = 0
    try:
        a = 1/0
    except:
        print('Erro')
        
except NameError as erro:
    print('Erro do desenvolvedor, fale com ele.', erro)
except (IndexError, KeyError) as erro:
    print('Erro de índice.')
except Exception as erro:
    print('Ocorreu um erro inesperado.')
else:
    pass
finally:
    a = ''

print(a)
print('Bora continuar...')