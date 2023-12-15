#DESENVOLVI ESSA CALCULADORA PARA PRATICAR OS CONCEITOS QUE APRENDI RECENTEMENTE EM PYTHON. PROCUREI USAR AS CONDIÇÕES, ESTRUTURAS DE REPETIÇÃO, LISTA E DICIONÁRIO

historico = []
count = 1

print("\n\n\n\n\nSEJA BEM-VINDO(A) AO --> CALCULADOR DESTEMIDO Ò.ó <-- !")
print("Escolha um valor, a operação desejada e outro valor. Assim haverá o cálculo desejado! =)")
print("_________________________________________________________________________________________")

while True:
    
    print(f"\n\nHORA DA {count}ª CONTINHA!")

    # OBTENDO O PRIMEIRO ELEMENTO
    n1 = float(input("\n\nDigite o primeiro valor: "))

    while True:
        
        # OBTENDO A ESCOLHA DE OPERAÇÃO DO USUÁRIO
        print("\n\nQual será o tipo de operação?")
        print("| 1 | -> SOMA")
        print("| 2 | -> SUBTRAÇÃO")
        print("| 3 | -> MULTIPLICAÇÃO")
        print("| 4 | -> DIVISÃO")
        o = int(input("Escolha o número que representa a operação que deseja: "))

        if 1 <= o <= 4:
            break
        else:
            print("\n\nOpa, calma lá! '-'\nVocê deve escolher um número correspondente com a operação que deseja: ")
            
    # OBTENDO O SEGUNDO ELEMENTO
    n2 = float(input("\n\nDigite o segundo valor: "))

    if o == 1:
        oEscolhida = "+"
        r = n1 + n2
        print(f"\nA soma entre {n1} e {n2} é igual a {r}")
    elif o == 2:
        oEscolhida = "-"
        r = n1 - n2
        print(f"\nA subtração entre {n1} e {n2} é igual a {r}")
    elif o == 3:
        oEscolhida = "x"
        r = n1 * n2
        print(f"\nA multiplicação entre {n1} e {n2} é igual a {r}")
    else:
        oEscolhida = "\u00F7"
        r = n1 / n2
        print(f"\nA divisão entre {n1} e {n2} é igual a {r}")
    
    registro = {"Conta de nº: ": count, "Valor anterior: " : n1, "Operação: " : oEscolhida, "Valor posterior ": n2, "RESULTADO: ": r}
    historico.append(registro)

    count += 1
    
    while True:
        print("\n\nGOSTARIA DE REALIZAR MAIS ALGUM CÁLCULO?")
        print("| 1 | -> Sim")
        print("| 2 | -> Não")
        repetir = int(input("Tecle um número correspondente a sua resposta: "))

        if repetir == 1:
            print("\n\nYES! Bora lá! =D")
            break
        elif repetir == 2:
            print("\n\nPoxa... Sentirei sua falta =(\nMe despeço então! Mas antes deixarei aqui o histórico das contas que fizemos juntos:")
            for item in historico:
                print(item)
            print("\nVALEU! FALOU!")
            exit()
        else:
            print("\nVocê parece cansado... Tecle um dos dois número para responder a pergunta a seguir, por favor.")





