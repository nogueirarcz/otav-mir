# Herança
class Pessoa:

    def __init__(self, nome, idade):

        self.nome = nome
        self.idade = idade
        self.nome_classe = self.__class__.__name__

    def falar(self):

        print(f'{self.nome_classe} está falando')


class Cliente(Pessoa):

    def comprar(self):

        print(f'{self.nome_classe} está comprando')


class Aluno(Pessoa):

    def estudar(self):

        print(f'{self.nome_classe} está estudando')


class ClienteVip(Cliente):

    # Sobrescrita de método construtor
    def __init__(self, nome, idade, sobrenome):

        super().__init__(nome, idade)
        
        self.sobrenome = sobrenome

    # Sobrescrita de método
    def falar(self):

        super().falar()
        print('* Falando *')
