from itertools import groupby, tee


alunos = [
    {'nome' : 'Luiz', 'nota': 'A'},
    {'nome' : 'Leticia', 'nota': 'B'},
    {'nome' : 'Fabricio', 'nota': 'A'},
    {'nome' : 'Rosemary', 'nota': 'C'},
    {'nome' : 'Joana', 'nota': 'D'},
    {'nome' : 'João', 'nota': 'A'},
    {'nome' : 'Eduardo', 'nota': 'B'},
    {'nome' : 'André', 'nota': 'A'},
    {'nome' : 'Anderson', 'nota': 'C'},
    {'nome' : 'José', 'nota': 'B'},
]

ordena = lambda item: item['nota']
alunos.sort(key=ordena)  # ordena os valores da lista de acordo com a nota
alunos_agrupados = groupby(alunos,ordena)  # agrupa os alunos por nota

for agrupamento, valores_agrupados in alunos_agrupados:
    va1, va2 = tee(valores_agrupados)
    print(f'Agrupamento: {agrupamento}')
    
    for aluno in va1:
        print(f'\t{aluno}')
    
    quantidade = len(list(va2))
    print(f'\t{quantidade} alunos tiraram a nota {agrupamento}')
    print()
  