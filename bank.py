#ESSE BANCO É PURAMENTE PARA TREINAR A POO (Programação orientada à objetos) NO PYTHON

class ContaBanco:
    
    def __init__(self):
        self.saldo = 0

    def mostrarSaldo(self):
        print(f"Saldo atual de R${self.saldo}")

    def sacar(self, valor):
        if valor > self.saldo:
            print(f"Saldo insuficiente para saque no valor de R${valor}\nSaque R${self.saldo} ou menos.")
        else :
            self.saldo -= valor
            print(f"Saque realizado no valor de R${self.saldo}.\n")
    
    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            print(f"Deposito realizado no valor de R${valor}\nSaldo atual de R${self.saldo}\n")
        else:
            print("Digite um valor acima de 0 para o deposito ser realizado.\n")

option = 0
info = ContaBanco()

print("\n\n---------------------SEJA BEM-VINDO(A) AO BANCO DOS EX-POBRES!---------------------")
print("\n")

while option != 4:
    print("\n--OPÇÕES DISPONÍVEIS DE OPERAÇÃO--")
    print("| 1 | -> MOSTRAR SALDO")
    print("| 2 | -> SACAR")
    print("| 3 | -> DEPOSITAR")
    print("| 4 | -> SAIR\n")

    option = int(input("\nTecle o número da operação solicitada: ")) 

    if option == 1:
        info.mostrarSaldo()
    elif option == 2:
        valor = float(input("\nDigite a quantidade em dinheiro que deseja sacar: R$ "))
        info.sacar(valor)
    elif option == 3:
        valor = float(input("\nDigite a quantidade em dinheiro que deseja depositar: R$ "))
        info.depositar(valor)
    elif option == 4:
        print("\nO BANCO DOS EX-POBRES AGRADECE SUA PREFERÊNCIA!\nATÉ A PRÓXIMA!")
        exit()
    else:
        print("\n\nERRO:\nNenhuma opção correspondente com o número teclado! Novamente...\n\n")  
