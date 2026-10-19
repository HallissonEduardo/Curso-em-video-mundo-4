class ContaBancaria:

    """
        Cria uma conta banacria e permite fazer saques e deposita.
    """

    def __init__(self, id: int, titular: str, saldo: float = 0):
        self.id = id
        self.titular = titular
        self.saldo = saldo

    def __str__(self):
        return f'A conta: {self.id} de {self.titular} tem R$ {self.saldo:.2f}'

    def deposito(self, valor: float) -> str:

        if valor > 0:
            self.saldo += valor
            return f"Deposito de R$ {valor:.2f} na conta {self.id}\n Saldo final  {self.saldo:.2f}"
        return "Erro: O valor do depósito deve ser maior que zero."

    def saque(self, valor: float) -> str:

        if valor > 0 and valor <= self.saldo:
            self.saldo -= valor
            return f"Saque de R$ {valor:.2f} na conta {self.id}\n Saldo final  {self.saldo:.2f}"

        if valor <= 0:
            return "Erro: O valor do saque deve ser maior que zero."
        return "Erro: Saldo insuficiente para realizar o saque."

#------------------------------------------------------------------------------
from dataclasses import dataclass


@dataclass
class Conta:
    conta: int = 0
    titular: str = ''
    saldo: float = 0.0

    def deposito(self, valor: float) -> str:

        if valor > 0:
            self.saldo += valor
            return f"deposito de {valor:.2f} na conta {self.conta}\n Saldo final  {self.saldo:.2f}"
        return "Erro: O valor do depósito deve ser maior que zero."

    def saque(self, valor: float) -> str:

        if 0 < valor <= self.saldo:
            self.saldo -= valor
            return f"Saque de {valor:.2f} na conta {self.conta}\n Saldo final  {self.saldo:.2f}"

        if valor <= 0:
            return "Erro: O valor do saque deve ser maior que zero."
        return "Erro: Saldo insuficiente."
