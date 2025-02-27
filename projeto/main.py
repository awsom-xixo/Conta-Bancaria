from conta import ContaCorrente

conta_lira = ContaCorrente('Lira','111-222-333-45') 
conta_lira.consultar_Saldo()

conta_lira.depositar_Dinheiro(1000)
conta_lira.consultar_Saldo()

conta_lira.sacar_Dinheiro(100)
conta_lira.consultar_Saldo()


