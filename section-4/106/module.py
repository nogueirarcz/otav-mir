# Setter -> configurar o valor de um atributo - Para ter um setter é necessário ter um getter
# Getter -> usado para obter o valor de um atributo

class Pessoa:

    def __init__(self, nome):

        self._nome = nome

    @property # Usado para definir um getter
    def nome(self):

        return self._nome

    @nome.setter # decorator para definir um
    def nome(self, nome):

        self._nome = nome


p1 = Pessoa('Guilherme')
p1.nome = 'Nogueira'
print(p1.nome)
