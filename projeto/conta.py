import datetime, pytz


class ContaCorrente():

    @staticmethod # Comentário que nos ajuda na organizção do código
    def _data_eHora():
        fusoBR = pytz.timezone('Brazil/East')
        horarioBR = datetime.datetime.now(fusoBR)
        return horarioBR.strftime('%d/%m/%Y %H:%M:%S') # Formata a data para ficar mais amigável para o usuário

# Parâmetros padrões da classe

    def __init__(self,nome,cpf, agencia, num_conta):
        self._nome = nome # Atributo privado
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

    def consultar_Transacoes(self):
        print('-' * (len('Histórico de transações: ')))
        print('Histórico de transações: ')
        for transacao in self.transacoes:
            print(transacao)

    def sacar_Dinheiro(self, valor):
        if (self.saldo - valor < self._limite_daConta()):
            print('Você não tem saldo suficiente para sacar esse valor.')
            self.consultar_Saldo()
        else:
            self.saldo -= valor
            self.registro_deTransacoes(-valor)
            self.consultar_Saldo()

    def depositar_Dinheiro(self,valor):
        self.saldo += valor
        self.registro_deTransacoes(valor)
        pass

    def transferir(self, valor, conta_destinada):
        self.saldo -= valor
        conta_destinada.saldo += valor
        self.registro_deTransacoes(valor)
        conta_destinada.registro_deTransacoes(valor)