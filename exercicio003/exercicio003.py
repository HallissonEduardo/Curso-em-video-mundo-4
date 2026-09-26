class ContaBancaria:

    """
        Cria uma conta banacria e permite fazer saques e deposita.
    """

    def __init__(self, id,
                 titular,
                 saldo = 0
                 ):

        self.id = id
        self.titular = titular
        self.saldo = saldo

    def __str__(self):
        return f'A conta:{self.id} de {self.titular} tem R${self.saldo:.2f}'


    def deposito(self, valor):
        if valor > 0:
            self.saldo += valor
            return f"Deposito de R$ {self.saldo:.2f} na conta {self.id}\n Saldo final  {self.saldo:.2f}"


    def saque(self, valor):
        if not valor > self.saldo:
            self.saldo -= valor
            return f"Saque de R$ {self.saldo:.2f} na conta {self.id}\n Saldo final  {self.saldo:.2f}"


#------------------------------------------------------------------------------
from dataclasses import dataclass


@dataclass
class Conta:

    conta: int = 0
    titular: str = ''
    saldo: float = 0

    def deposito (self, valor: float)-> str:
        self.saldo += valor
        return f"deposito de {valor} na conta {self.conta}\n Saldo final  {self.saldo:.2f}"


    def saque (self, valor: float)-> str:
        self.saldo -= valor
        return f"Saque de {valor} na conta {self.conta}\n Saldo final  {self.saldo:.2f}"



if __name__ == '__main__':
    g1 = ContaBancaria(id = 112,
                       titular = 'Hallisson',
                       saldo = 100
                       )
    #print(g1)
    #print(g1.__doc__)
    #g1.deposito(1000)
    #g1.saque(19)
    #print(g1)
    #print(g1.saque(20))
    #print(g1.saque(30))
    #print(g1.deposito(37))
    #print(g1.saque(50))

    print('-' * 40)

    c1 = Conta(101,
               "Hallisson",
               1010)

    print(c1.deposito(100))
    print(c1.saque(99))