#AQUI EU SÓ ESTAVA CUMPRINDO UM DESAFIO QUE VI NA INTERNET SOBRE POO. APENAS PARA FIXAÇÃO DO TEMA MESMO.
print("\n\nBEM-VINDO(A) AO ANALISADOR DE FRASES!\n")

class Phrase:

    def __init__(self) -> None:
        self.frase = input("Insira uma frase qualquer para que haja a análise da mesma\n-> ")

    def countCaracteres(self):
        self.qtd_caracteres = len(self.frase)
        print(f"Quantidade de caracteres nessa frase: {self.qtd_caracteres}\n")

    def countPalavras(self):
        palavras = self.frase.split()
        self.qtd_palavras = len(palavras)
        print(f"Quantidade de palavras nessa frase: {self.qtd_palavras}\n")

    def inverterFrase(self):
        frase_invertida = self.frase[::-1]
        print(f"Inversão da frase inserida: '{frase_invertida}'\n")

dados = Phrase()

print("\nCERTO, CERTO... Hora de analisar a sua frase!\n")
print(f"Frase inserida: '{dados.frase}'\n")
dados.countCaracteres()
dados.countPalavras()
dados.inverterFrase()