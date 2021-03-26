"""
Getter = obtém um valor
setter = configura um valor ("filto" -> evita problemaw com os atributos de uma classe)

Getter e setter podem ser entendidos como uma proteção para o atributo de uma classe.
@property = decorador em python
"""


class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def desconto(self, percentual):
        self.preco = self.preco - (self.preco * (percentual / 100))


    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, valor):
        self._nome = valor.lower()
    # Getter
    @property
    def preco(self):
        return self._preco

    # Setter
    @preco.setter
    def preco(self, valor):
        if isinstance(valor, str):  # Checa se valor é uma instância de string
            valor = float(valor.replace('R$',''))

        self._preco = valor

p1 = Produto('Camiseta', 50)
p1.desconto(10)
print(p1.nome, p1.preco)

p2 = Produto('Caneca', 15)
p2.desconto(10)
print(p2.nome, p2.preco)
