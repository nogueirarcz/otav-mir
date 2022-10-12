# Associação em Python OO

class Escritor:

    def __init__(self, nome):

        self._nome = nome
        self._ferramenta = None

    @property # Getter
    def nome(self):

        return self._nome

    @property # Getter
    def ferramenta(self):

        return self._ferramenta

    @ferramenta.setter # Setter
    def ferramenta(self, ferramenta):

        self._ferramenta = ferramenta


class Caneta:

    def __init__(self, marca):

        self._marca = marca

    @property # Getter
    def marca(self):

        return self._marca

    def escrever(self):

        print('Caneta está escrevendo...')


class MaquinaDeEscrever:

    def escrever(self):

        print('Máquina está escrevendo...')
