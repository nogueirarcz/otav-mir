# Herança Múltipla
class A:

    def falar(self):

        print('Falando em A')


class B(A):

    def falar(self):

        print('Falando em B')


class C(A):

    def falar(self):

        print('Falando em C')


# Herança Múltipla
class D(B, C):

    ...
    