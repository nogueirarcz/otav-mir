from eletronico import Eletronico
from log import LogMixin


class Smartphone(Eletronico, LogMixin):

    def __init__(self, nome):

        super().__init__(nome)
        self._conectado = False

    def conectar(self):

        if not self._ligado:

            error = (f'{self._nome} não está ligado. *impossível conectar!*')
            self.log_error(error)
            return

        if self._conectado:

            error = (f'{self._nome} já está conectado. *Operação redundante*')
            self.log_error(error)
            return

        self._conectado = True
        info = (f'{self._nome} acaba de se conectar.')
        self.log_info(info)

    def desconectar(self):

        if not self._conectado:

            error = (f'{self._nome} não está conectado. *Operação redundante*')
            self.log_error(error)
            return

        info = (f'{self._nome} acaba de desconectar-se')
        self.log_info(info)
        self._conectado = False
        