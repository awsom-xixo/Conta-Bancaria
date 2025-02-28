import datetime
import pytz


class ContaCorrente:
    @staticmethod  # Comentário que nos ajuda na organização do código
    def _data_e_hora():
        fuso_br = pytz.timezone('Brazil/East')
        horario_br = datetime.datetime.now(fuso_br)
        return horario_br.strftime('%d/%m/%Y %H:%M:%S')  # Formata a data para ficar mais amigável para o usuário

    # Parâmetros padrão da classe
    def __init__(self, nome, cpf, agencia, num_conta):
        self._nome = nome
        self._cpf = cpf
        self._saldo = 0  # Atributo interno
        self._limite = None  # Atributo interno
        self._agencia = agencia
        self._num_conta = num_conta
        self._transacoes = []  # Atributo interno
        self._cartoes = []

    def registro_de_transacoes(self, valor):
        self._transacoes.append((valor, self._saldo, ContaCorrente._data_e_hora()))

    def _limite_da_conta(self):  # Método privado
        self._limite = -1000
        return self._limite

    def consultar_Saldo(self):
        print('Seu saldo atual é de R${:,.2f}'.format(self._saldo))

    def consultar_Transacoes(self):
        print('-' * len('Histórico de transações: '))
        print('Histórico de transações: ')
        for transacao in self._transacoes:
            print(transacao)

    def sacar_Dinheiro(self, valor):
        if self._saldo - valor < self._limite_da_conta():
            print('Você não tem saldo suficiente para sacar esse valor.')
            self.consultar_saldo()
        else:
            self._saldo -= valor
            self.registro_de_transacoes(-valor)
            self.consultar_Saldo()

    def depositar_Dinheiro(self, valor):
        self._saldo += valor
        self.registro_de_transacoes(valor)

    def transferir(self, valor, conta_destinada):
        self._saldo -= valor
        conta_destinada._saldo += valor  # Corrigido o acesso ao saldo da conta destinatária
        self.registro_de_transacoes(-valor)
        conta_destinada.registro_de_transacoes(valor)



class CartaoCredito:

    @staticmethod # Comentário que nos ajuda na organizção do código
    def _data_eHora():
        fusoBR = pytz.timezone('Brazil/East')
        horarioBR = datetime.datetime.now(fusoBR)
        return horarioBR.strftime('%d/%m/%Y %H:%M:%S') # Formata a data para ficar mais amigável para o usuário

    def __init__(self, titular, conta_corrente):
        self.numero = None
        self.titular = titular
        self.validade = None
        self.cod_seguranca = None 
        self.limite = None
        self.conta_corrente = conta_corrente
        conta_corrente._cartoes.append(self) # Adiciona a lista toda a instância



class Agencia(): # cria uma classe agencia
    
    def __init__(self, telefone, cnpj, numero): # inicializa com os atributos telefone, cnpj e numero
        self.telefone = telefone
        self.cnpj = cnpj
        self.numero = numero
        self.clientes = []  # lista com os clientes
        self.caixa = 0
        self.emprestimos = [] # lista com os emprestimos
        
    def verificar_caixa(self): # função para verificar o caixa
        if self.caixa < 1000000:
            print(f"Caixa abaixo do nivel recomendado. Caixa atual:R${self.caixa}")
        else:
            print(f"O valor do caixa esta OK. Caixa atual:R${self.caixa}")

    def emprestar_dinheiro(self, valor, cpf, juros):#função para emprestar dinheiro
        if self.caixa > 1000000:
            self.emprestimos.append((valor, cpf, juros))
            print("Emprestimo efetuado!")
        else:
            print("Emprestimo negado!")

    def adicionar_cliente(self, nome, cpf, patrimonio): # Função para adicionar clientes a lista criada
        self.clientes.append((nome, cpf, patrimonio)) # Adiciona os clientes a lista



class AgenciaVirtual(Agencia): # Uma outra agencia porem herda as caracteristicas da classe mãe
    
    def __init__(self, site, telefone, cnpj, numero): # Inicializa com os atributos site, telefone cnpj e numero
        self.site = site
        super().__init__(telefone, cnpj, numero) # Herdando os atributos telefone, cnpj e numero da classe mãe
        self.caixa_paypal = 0

    def depositar_paypal(self, valor): # Função para deposito
        self.caixa -= valor # Tira valor do caixa
        self.caixa_paypal += valor # Adiciona valor ao "paypal"

    def saque_paypal(self, valor): # Função de saque
        self.caixa += valor # Adiciona valor ao caixa
        self.caixa_paypal -= valor # Retira valor do "paypal"

    def adicionar_cliente(self, nome, cpf, patrimonio):
        super().adicionar_cliente(nome, cpf, patrimonio) 



class AgenciaComum(Agencia): # Agencia comum herdando a classe AGENCIA
    
    def __init__(self, telefone, cnpj, numero): # Inicializa com esses atributos
        super().__init__(telefone, cnpj, numero) # Herda esses atributos
        self.caixa = 1000000
    
    def adicionar_cliente(self, nome, cpf, patrimonio):
        super().adicionar_cliente(nome, cpf, patrimonio) # Pega a função adicionar_cliente da classe mae



class AgenciaPremium(Agencia): # Terceira agencia que herda caracteristicas da classe mae

    def __init__(self, telefone, cnpj, numero): # Inivializa com esses atributos
        super().__init__(telefone, cnpj, numero) # Herda esses atributos
        self.caixa = 10000000

    def adicionar_cliente(self, nome, cpf, patrimonio):
        if patrimonio > 1000000:
            super().adicionar_cliente(nome, cpf, patrimonio) # Pega a função adicionar_cliente da classe mae
        else:
            print("Cliente não possui o patrimonio minimo necessario") # Caso nao tenha patrimonio o suficiente