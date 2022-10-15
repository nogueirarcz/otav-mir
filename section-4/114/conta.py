from abc import ABC, abstractclassmethod, abstractmethod


class Conta(ABC):

    def __init__(self, agencia, conta, saldo):

        self._agencia = agencia
        self._conta = conta
        self._saldo = saldo

    @property
    def agencia(self):

        return self._agencia

    @property
    def conta(self):

        return self._conta

    @property
    def saldo(self):

        return self._saldo
    
    @saldo.setter
    def saldo(self, valor):

        if not isinstance(valor, (int, float)):

            raise ValueError('O valor precisa ser numérico!')

        self._saldo = valor
        
    def depositar(self, valor):

        if not isinstance(valor, (int, float)):

            raise ValueError('O valor do depósito precisa ser numérico')

        self._saldo += valor
        self.ver_detalhes()

    def ver_detalhes(self):

        print(f'Agência: {self.agencia}\nConta: {self.conta}\nSaldo: {self.saldo}')

    @abstractmethod
    def sacar(self, valor):

        ...
