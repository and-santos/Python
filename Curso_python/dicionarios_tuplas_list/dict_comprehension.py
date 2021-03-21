lista = [
    ('chave','valor'),
    ('chave2','valor2'),
]

d1 = {x: y for x, y in enumerate(range(5))}


d1 = {x for x in range(5)}  # compreensão de sets
print(d1, type(d1))

d1 = {f'chave_{x}': x**2 for x in range(5)}
print(d1)