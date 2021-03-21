
carrinho = []

carrinho.append(('Produto 1', 20))
carrinho.append(('Produto 2', 30))
carrinho.append(('Produto 3', 50))
carrinho.append(('Produto 4', 60))

"""
total = 0 
for produto in carrinho:
    total += produto[1]

total = []
for produto in carrinho:
    total.append(produto[1])
"""

# Solução
total = sum([float(produto[1]) for produto in carrinho])
print(total)
# Solução 2
total2 = sum([float(y) for x, y in carrinho])
print(total2)

"""
Faça a soma de todos os itens do carrinho usando list comprehension
"""
