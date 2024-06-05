#Faça uma função que receba 2 listas de valores inteiros e retorne a lista DIFERENÇA.
def diferenca1(lista1, lista2):
    listadiferenca1=[]
    for i in range(len(lista1)):
        if lista1[i] not in lista2:
            listadiferenca1.append(lista1[i])
    return listadiferenca1
def diferenca2(lista1, lista2):
    listadiferenca2=[]
    for i in range(len(lista2)):
        if lista2[i] not in lista1:
            listadiferenca2.append(lista2[i])
    return listadiferenca2
def main():
    lista1=[]
    lista2=[]
    valor1=int(input("Escolha a quantidade de elementos da lista 1: "))
    valor2=int(input("Escolha a quantidade de elementos da lista 2: "))
    for i in range(valor1):
        num=float(input("Escolha um número: "))
        lista1.append(num)
    for i in range(valor2):
        num=float(input("Escolha um número: "))
        lista2.append(num)
    listadiferenca1=diferenca1(lista1,lista2)
    listadiferenca2=diferenca2(lista1,lista2)
    print(f"A diferença da lista 1 {lista1} com a lista 2 {lista2} é = {listadiferenca1}")
    print(f"A diferença da lista 2 {lista2} com a lista 1 {lista1} é = {listadiferenca2}")
main()