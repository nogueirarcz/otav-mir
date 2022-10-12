'''
    Encapsulamento com Python

    O encapsulamento em Python funciona de maneira diferente das outras linguagens OO
'''

'''
    Convenção

    Usando 1 underscore _ --> Recomenda-se que não acesse (Protected)
    Usando 2 underscore __ -> Recomenda-se fortemente não acessar (Private)
'''

class BaseDeDados:

    def __init__(self):

        self.dados = {}

    def inserir_cliente(self, id, nome):

        if 'clientes' not in self.dados:

            self.dados['clientes'] = {id: nome}
        
        else:

            self.dados['clientes'].update({id: nome})

    def lista_clientes(self):
        
        for id, nome in self.dados['clientes'].items():

            print(id, nome)

    def apaga_cliente(self, id):

        del self.dados['clientes'][id]


bd = BaseDeDados()

bd.inserir_cliente(1, 'Otávio')
bd.inserir_cliente(2, 'Miranda')
bd.lista_clientes()
print(bd.dados)
