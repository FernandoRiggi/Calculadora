#Faça uma função que receba uma lista como parâmetro e retorne sua soma.
def somalista(lista):
    i=0
    soma=0
    for i in range(len(lista)):
        soma+=lista[i]
    return soma
def main():
    valor = int(input("Digite quantos elementos você deseja adicionar na frase: "))
    lista=[]
    for i in range(valor):
        num=float(input("Digite um número: "))
        lista.append(num)
    ressoma=somalista(lista)
    print(f"O resultado da soma da lista é = {ressoma}")
main()