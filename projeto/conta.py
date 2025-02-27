import datetime, pytz


class ContaCorrente():

    @staticmethod # Comentário que nos ajuda na organizção do código
    def _data_eHora():
        fusoBR = pytz.timezone('Brazil/East')
        horarioBR = datetime.now(fusoBR)
        return horarioBR

# Parâmetros padrões da classe

    def __init__(self,nome,cpf, agencia, num_conta):
        self.nome = nome
        self.cpf = cpf
        self.saldo = 0 # Atributo interno
        self.limite = None # Atributo interno
        self.agencia = agencia
        self.num_conta = num_conta
        self.transacoes = [] # Atributo interno

    def registro_deTransacoes(self,valor):
        self.transacoes.append((valor, self.saldo, ContaCorrente._data_eHora()))
        pass

    def _limite_daConta(self): # Método privado
        self.limite = -1000
        return self.limite

    def consultar_Saldo(self):
        print('Seu saldo atual é de R${:,.2f}'.format(self.saldo))
        pass

    def sacar_Dinheiro(self,valor): # Valor = parâmetro
        if (self.saldo < self._limite_daConta()):
            print('Você não tem saldo suficiente para sacar esse valor. ')
            self.consultar_Saldo() # Usando um método dentro de outro
        else:
            self.saldo -= valor
            self.registro_deTransacoes(valor)
            self.consultar_Saldo()
        pass

    def depositar_Dinheiro(self,valor):
        self.saldo += valor
        self.registro_deTransacoes(valor)
        pass
