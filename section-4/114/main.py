from conta_corrente import ContaCorrente
from conta_poupanca import ContaPoupanca


conta1 = ContaPoupanca(13, 2211, 0)
conta1.depositar(100)
conta1.sacar(50)

print('')

cc1 = ContaCorrente(agencia=1111, conta=3333, saldo=0, limite=500)
cc1.sacar(120)
