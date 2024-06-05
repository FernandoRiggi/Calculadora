#Faça uma função que receba 2 listas de valores inteiros, o modo de saída (U:união, I:intersecção, D:diferença) e retorne a lista resultante.
def uniao(lista1, lista2):
    listauniao=[]
    for i in range(len(lista1)):
        listauniao.append(lista1[i])
    for i in range(len(lista2)):
        if lista2[i] not in listauniao:
            listauniao.append(lista2[i])
    return listauniao
def interseccao(lista1, lista2):
    listaintersseccao=[]
    for i in range(len(lista1)):
        if lista1[i] in lista2:
            listaintersseccao.append(lista1[i])
    return listaintersseccao
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
def menu():
    print("Escolha uma opção de 1 até 4 ou digite 5 para sair")
    print('1. União')
    print('2. Intersecção')
    print("3. Diferença lista1")
    print("4. Diferença lista2")
    print("5. Sair")
    op=int(input("Escolha a opção que deseja realizar: "))
    return op
def main():
    operação=1
    while operação !=5:
        operação=menu() #mostrar menu
        if operação==1: #uniao
            lista1=[]
            lista2=[]
            valor1=int(input("Escolha quantos elementos a lista 1 terá: "))
            valor2=int(input("Escolha quantos elemetnos a lista 2 terá: "))
            for i in range(valor1):
                num=float(input("Escolha um número: "))
                lista1.append(num)
            for i in range(valor2):
                num=float(input("Escolha um número: "))
                lista2.append(num)
            listauniao=uniao(lista1,lista2)
            print(f"A união da lista 1 {lista1} com a lista 2 {lista2} é = {listauniao}")
        elif operação==2: #intersecção
            lista1=[]
            lista2=[]
            valor1=int(input("Escolha quantos elementos a lista 1 terá: "))
            valor2=int(input("Escolha quantos elemetnos a lista 2 terá: "))
            for i in range(valor1):
                num=float(input("Escolha um número: "))
                lista1.append(num)
            for i in range(valor2):
                num=float(input("Escolha um número: "))
                lista2.append(num)
            listainterseccao=interseccao(lista1,lista2)
            print(f"A intersecção da lista 1 {lista1} com a lista 2 {lista2} é = {listainterseccao}")
        elif operação==3: #diferença1
            lista1=[]
            lista2=[]
            valor1=int(input("Escolha quantos elementos a lista 1 terá: "))
            valor2=int(input("Escolha quantos elemetnos a lista 2 terá: "))
            for i in range(valor1):
                num=float(input("Escolha um número: "))
                lista1.append(num)
            for i in range(valor2):
                num=float(input("Escolha um número: "))
                lista2.append(num)
            listadiferenca1=diferenca1(lista1,lista2)
            print(f"A diferença da lista 1 {lista1} com a lista 2 {lista2} é = {listadiferenca1}")
        elif operação==4: #diferença2
            lista1=[]
            lista2=[]
            valor1=int(input("Escolha quantos elementos a lista 1 terá: "))
            valor2=int(input("Escolha quantos elemetnos a lista 2 terá: "))
            for i in range(valor1):
                num=float(input("Escolha um número: "))
                lista1.append(num)
            for i in range(valor2):
                num=float(input("Escolha um número: "))
                lista2.append(num)
            listadiferenca2=diferenca2(lista1,lista2)
            print(f"A diferença da lista 2 {lista2} com a lista 1 {lista1} é = {listadiferenca2}")
        elif operação==5: #sair
            print("Encerrando programa")
        else:
            print("Operação invalida. Escolha uma opção de 1 até 5")
main()