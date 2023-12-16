#ESSE BANCO É PURAMENTE PARA TREINAR A POO (Programação orientada à objetos) NO PYTHON

print("\n\n---------------------SEJA BEM-VINDO(A) AO BANCO DOS EX-POBRES!---------------------")
print("\n")

#TREINANDO O CONSTRUCTOR
class Pessoa:
    # AQUI CASO EU QUISESSE PASSAR OS VALORES DO ATRIBUTO DA CLASSE DIRETAMENTE
    """
    def __init__(self, CPF:int, nome:str, dataNascimento:str) -> None:
            self.CPF = CPF
            self.nome = nome
            self.dataNascimento = dataNascimento
    """
    #MAS VAMOS DEIXAR O USUÁRIO NOS CONTAR QUAL O VALOR DE CADA UM :)
    def __init__(self) -> None:
        self.CPF = int(input("Informe seu CPF, mas sem utilizar '.' ou '-'.\nExemplo: 12345678909\nInsira agora o CPF, por gentileza-> "))
        self.nome = input("Informe seu nome completo-> ")
        self.dataNascimento = input("Informe sua data de nascimento (no formato DD/MM/AAAA) -> ")

p = Pessoa()

class ContaBanco:
    
    def __init__(self):
    #TORNANDO O SALDO PRIVADO COM '__'. ASSIM TORNO MAIS SEGURO DE MANIPULAÇÕES EXTERNAS
        self.__saldo = 0
    #CRIANDO OS MÉTODOS DA CLASSE
    def mostrarExtrato(self):
        print(f"\nNome: {p.nome}")
        print(f"Data de nascimento: {p.dataNascimento}")
        print(f"CPF: {p.CPF}")
        print(f"Saldo atual de R${self.__saldo:.2f}\n")

    def sacar(self, valor):
        if valor > self.__saldo:
            print(f"Saldo insuficiente para saque no valor de R${valor:.2f}\n")
        else :
            self.__saldo -= valor
            print(f"Valor sacado de R${valor:.2f} com sucesso!\n")
            print(f"Saldo atual de R${self.__saldo:.2f}.\n")
    
    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
            print(f"Depósito realizado no valor de R${valor:.2f}\nSaldo atual de R${self.__saldo:.2f}\n")
        else:
            print("Digite um valor acima de 0 para o deposito ser realizado.\n")
    
option = 0

info = ContaBanco()

while option != 4:
    print("\n--OPÇÕES DISPONÍVEIS DE OPERAÇÃO--")
    print("| 1 | -> EXTRATO")
    print("| 2 | -> SACAR")
    print("| 3 | -> DEPOSITAR")
    print("| 4 | -> SAIR\n")

    option = int(input("\nTecle o número da operação solicitada: ")) 

    if option == 1:
        info.mostrarExtrato()
    elif option == 2:
        valor = float(input("\nDigite a quantidade em dinheiro que deseja sacar: R$ "))
        info.sacar(valor)
    elif option == 3:
        valor = float(input("\nDigite a quantidade em dinheiro que deseja depositar: R$ "))
        info.depositar(valor)
    elif option == 4:
        print(f"\nO BANCO DOS EX-POBRES AGRADECE SUA PREFERÊNCIA!\nAté a próxima, {p.nome}!")
        exit()
    else:
        print("\n\nERRO:\nNenhuma opção correspondente com o número teclado! Novamente...\n\n")  
