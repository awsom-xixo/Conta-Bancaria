from conta import ContaCorrente

conta_lira = ContaCorrente('Lira', '111-222-333-45', 4444, 12345)
conta_maeLira = ContaCorrente('Beth', '222-333-444-56', 5555, 23456)

conta_lira.consultar_Saldo()
conta_maeLira.depositar_Dinheiro(100)
conta_maeLira.consultar_Saldo()
conta_lira.depositar_Dinheiro(10000)

conta_lira.sacar_Dinheiro(100)

conta_lira.transferir(1000, conta_maeLira)
conta_maeLira.consultar_Saldo()


print('Saldo final:')
conta_lira.consultar_Saldo()

conta_lira.consultar_Transacoes()

