from pessoa import Pessoa

p1 = Pessoa('Luiz', 29)  # instância da classe Pessoa

p2 = Pessoa('João', 32)

p1.falar('POO')
p2.falar('Filmes')
p1.comer('churrasco')

print(p1.get_ano_nascimento())
print(p2.get_ano_nascimento())
