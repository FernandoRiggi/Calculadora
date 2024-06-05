#Elabore a função Inteiro(n) que verifica se o valor de entrada é um
#número inteiro e retorna Verdadeiro em caso afirmativo e Falso caso contrário.
def Inteiro(n):
    for i in n:
        if not ",.;":
            return True
        else:
            return False
def main():
    n=input("Escolha um número: ")
    inteiro = Inteiro(n)
    print(f"{inteiro}")
main()