#Faça uma função que receba 2 listas de valores inteiros e retorne a lista UNIÃO.
def uniao(lista1, lista2):
    listauniao=[]
    for i in range(len(lista1)):
        listauniao.append(lista1[i])
    for i in range(len(lista2)):
        if lista2[i] not in listauniao:
            listauniao.append(lista2[i])
    return listauniao
def main():
    lista1=[]
    lista2=[]
    valor1=int(input("Digite a quantidade de elementos deseja que a lista1 tenha: "))
    valor2=int(input("Digite a quantidade de elementos deseja que a lista2 tenha: "))
    for i in range(valor1):
        num=float(input("Escolha um número: "))
        lista1.append(num)
    for i in range(valor2):
        num=float(input("Escolha um número: "))
        lista2.append(num)
    listauniao=uniao(lista1, lista2)
    print(f"A união da lista1 {lista1} com a lista2 {lista2} é = {listauniao}")
main()