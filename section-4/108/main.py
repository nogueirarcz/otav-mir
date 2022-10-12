# Associação em Python OO
from classes import Escritor
from classes import Caneta
from classes import MaquinaDeEscrever


esc1 = Escritor('Jhon')
print(esc1.nome)

can1 = Caneta('Bic')
print(can1.marca)

maq1 = MaquinaDeEscrever()
print(maq1)

esc1.ferramenta = can1
esc1.ferramenta.escrever()
