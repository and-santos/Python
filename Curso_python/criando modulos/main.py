
from vendas.calc_preco import aumento, reducao
import vendas.formata.preco as formata

preco = 49.90

preco_com_aumento = aumento(valor = preco, porcentagem = 15, formata=True)
print(preco_com_aumento)

preco_com_reducao = reducao(valor=preco, porcentagem=15, formata=True)
print(preco_com_reducao)

print(formata.real(50))