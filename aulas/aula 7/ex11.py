#Faça uma função que receba 2 listas de valores inteiros e retorne a lista INTERSECÇÃO
def interseccao(lista1, lista2):
    listaintersseccao=[]
    for i in range(len(lista1)):
        if lista1[i] in lista2:
            listaintersseccao.append(lista1[i])
    return listaintersseccao
def main():
    lista1=[]
    lista2=[]
    valor1=int(input("Escolha quantos elementos deseja que a lista1 tenha: "))
    valor2=int(input("Escolha quantos elementos deseja que a lista2 tenha: "))
    for i in range(valor1):
        num=float(input("Escolha um número: "))
        lista1.append(num)
    for i in range(valor2):
        num=float(input("Escolha um número: "))
        lista2.append(num)
    listaintersseccao=interseccao(lista1, lista2)
    print(f"A intersecção da lista1 {lista1} com a lista2 {lista2} é = {listaintersseccao}")
main()