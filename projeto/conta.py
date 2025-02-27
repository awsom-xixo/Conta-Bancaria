class ContaCorrente():
# Parâmetros padrões da classe
    def __init__(self,nome,cpf):
        self.nome = nome
        self.cpf = cpf
        self.saldo = 0 # Atributo interno

    def consultar_Saldo(self):
        print('Seu saldo atual é de R${:,.2f}'.format(self.saldo))
        pass

    def sacar_Dinheiro(self,valor): # Valor = parâmetro
        self.saldo -= valor
        pass

    def depositar_Dinheiro(self,valor):
        self.saldo += valor
        pass
