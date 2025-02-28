from classes import CartaoCredito, ContaCorrente, Agencia, AgenciaVirtual, AgenciaPremium, AgenciaComum
import os
import random


def limpa(): # Por capricho foi criado uma função que limpa o terminal.
    os.system("cls" if os.name == "nt" else "clear")

conta_micael = ContaCorrente("Micael", "130.999.160-45", "12445", "8922430")
conta_vitor = ContaCorrente("Vitor", "123.139.456-02", "75319", "912341")

# Depositar dinheiro
conta_micael.depositar_Dinheiro(1000)
conta_micael.consultar_Saldo()

# Sacando dinheiro
conta_micael.sacar_Dinheiro(250)
conta_micael.consultar_Saldo()
conta_micael.consultar_Transacoes()
conta_micael.transferir(200, conta_vitor)
cartao_micael = CartaoCredito("Micael", conta_micael)
print(cartao_micael.numero, cartao_micael.titular, cartao_micael.validade, cartao_micael.cod_seguranca, cartao_micael.limite)

print(cartao_micael.__dict__)

# Criando uma agência
agencia1 = Agencia("22223333", "200000000", "4568")

agencia1.caixa = 10000000

print(agencia1.__dict__)
agencia1.verificar_caixa()
agencia1.emprestar_dinheiro(10, "11122233344", 0.1)

agencia1.adicionar_cliente("Micael", "132509524711", 100000)
print(agencia1.clientes)

# Criando uma agência virtual
agencia_virtual = AgenciaVirtual("www.agencia_virtual.com.br@yahoobrasil.wisx", "22224444", "152000000000", "99912312")
agencia_virtual.verificar_caixa()
print(agencia_virtual.__dict__)

# Criando uma agência comum
agencia_comum = AgenciaComum("33334444", "222000000000000", random.randint(1001, 9999))
agencia_comum.verificar_caixa()
print(agencia_comum.__dict__)

# Criando uma agência premium
agencia_premium = AgenciaPremium("333333333", "3000000000", random.randint(1001, 9999))
print("Agencia premium: ")
print(agencia_premium.__dict__)

# Testando a função "paypal" da agência virtual
agencia_virtual.depositar_paypal(2000)
print(agencia_virtual.caixa)
print(agencia_virtual.caixa_paypal)

# Adicionando clientes em todas as agências
agencia1.adicionar_cliente("Micael", "1111111111111", 1000000)
print(f"Clientes agencia1: {agencia1.clientes}")

agencia_virtual.adicionar_cliente("Micael", "1111111111111", 1000000)
print(f"Clientes agencia virtual: {agencia_virtual.clientes}")

agencia_comum.adicionar_cliente("Micael", "1111111111111", 1000000)
print(f"Clientes agencia comum: {agencia_comum.clientes}")

agencia_premium.adicionar_cliente("Micael", "111111111111", 1000000)
print(f"Clientes agencia premium: {agencia_premium.clientes}")