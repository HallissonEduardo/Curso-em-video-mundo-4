from exercicio003 import ContaBancaria, Conta



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