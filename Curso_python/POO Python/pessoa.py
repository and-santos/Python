# A palavra-chave "self" é obrigatório, presente em todos os métodos
#  e faz referência a instância da classe.
# Isto é, faz referência ao objeto no qual é atribuido a classe
# Cada classe deve conter o método especial chamado __init__

from datetime import datetime

class Pessoa:
    ano_atual = int(datetime.strftime(datetime.now(), '%Y'))

    def __init__(self, nome, idade, comendo=False, falando=False):
        self.nome = nome
        self.idade = idade
        self.comendo = comendo
        self.falando = falando

    def falar(self, assunto):
        if self.comendo:
            print(f'{self.nome} não pode falar comendo.')
            return

        if self.falando:
            print(f'{self.nome} já está falando.')
            return
            
        print(f'{self.nome} está falando sobre {assunto}.')
        self.falando = True

    def parar_falar(self):
       if not self.falando:
           print(f'{self.nome} já está falando')
           return 


    def comer(self, alimento):
        if self.comendo:
            print(f'{self.nome} já está comendo.')
            return
       
        if self.falando:
           print(f'{self.nome} não pode comer falando.')
           return

        print(f'{self.nome} está comendo {alimento}.')
        self.comendo = True

    def parar_comer(self):
        if not self.comendo:
            print(f'{self.nome} não está comendo.')
            return

        print(f'{self.nome} parou de comer.')
        self.comendo = False

    def get_ano_nascimento(self):
        return self.ano_atual - self.idade