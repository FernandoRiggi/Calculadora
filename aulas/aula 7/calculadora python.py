def somar(lista):
# Esta função recebe uma lista de números e retorna a soma de todos os números na lista.
    soma = 0
    for numero in lista:
        soma += numero
    return soma
def subtrair(lista):
# Esta função recebe uma lista de números e retorna a subtração de todos os números na lista, começando pelo primeiro número.
    subtracao= lista[0]
    for numero in lista[1:]:
        subtracao -= numero
    return subtracao
def multiplicar(lista):
# Esta função recebe uma lista de números e retorna a multiplicação de todos os números na lista.
    multiplicacao=lista[0]
    for numero in lista[1:]:
        multiplicacao *= numero
    return multiplicacao
def dividir(lista):
# Esta função recebe uma lista de números e retorna a divisão de todos os números na lista, começando pelo primeiro número.
# Se algum número na lista for 0, a função imprime uma mensagem de erro e retorna None.
    divisao=lista[0]
    for numero in lista[1:]:
        if numero !=0:
            divisao /= numero
        else:
            print("Divisão invalidada, pois foi dividida por 0")
            return None
    return divisao
def potenciar(base,expoente):
# Esta função recebe uma base e um expoente e retorna a base elevada ao expoente.
    potencia = base**expoente
    return potencia
def raizquadrada(n):
# Esta função recebe um número e retorna a raiz quadrada do número.
# Se a raiz quadrada não for um número inteiro, a função imprime uma mensagem de erro e retorna None.
    raiz = n**0.5
    if raiz == int(raiz):
        return raiz
    else:
        print("Não há raiz quadrada inteira")
        return None
def menu():
    print("Escolha uma opção de 1 até 6, ou digite 7 para sair")
    print("1. somar")
    print("2. subtrair")
    print("3. multiplicar")
    print("4. dividir")
    print("5. potenciação")
    print("6. raiz quadrda")
    print("7. sair")
    op=int(input("Escolha a opção que deseja realizar: "))
    return op
def main():
    operacao= 1
    while operacao !=7:
        operacao = menu() #mostrar o menu
        if operacao == 1: #soma
            valor = int(input("Escolha quantos números deseja somar: "))#valor limite para o loop
            i=0
            listasoma=[]
            while i<valor:
                n=float(input("Escolha um número: "))
                listasoma.append(n)
                i+=1
            res =somar(listasoma)
            print(f"Soma = {res}")
        elif operacao ==2: #subtração
            valor = int(input("Escolha quantos números desaja subtrair: "))#valor limite para o loop
            i = 0
            listasubtração=[]
            while i<valor:
                n=float(input("Escolha um número: "))
                listasubtração.append(n)
                i+=1
            res = subtrair(listasubtração)
            print(f"Subtração = {res}")
        elif operacao ==3: #multiplicação
            valor =int(input("Escolha quantos números deseja multiplicar: "))#valor limite para o loop
            i=0
            listamultiplicacao=[]
            while i<valor:
                n=float(input("Escolha um número: "))
                listamultiplicacao.append(n)
                i+=1
            res = multiplicar(listamultiplicacao)
            print(f"Multiplicação = {res}")
        elif operacao ==4: #divisão
            valor = int(input("Escolha quantos números deseja dividir: ")) #valor limite para o loop
            i=0
            listadivisao=[]
            while i<valor:
                n=float(input("Escolha um número: "))
                listadivisao.append(n)
                i+=1
            res = dividir(listadivisao)
            print(f"Divisão = {res}")
        elif operacao ==5: #potenciação
            base = int(input("Escolha o número que será a base: "))
            expoente=int(input("Escolha o número que será o expoente:"))            
            res = potenciar(base,expoente)
            print(f"{base} elevado a {expoente} é = {res}")
        elif operacao ==6: #raizquadrada
            n=int(input("Escolha o número que deseja descobrir a raiz: "))
            res=raizquadrada(n)
            print(f"A raiz quadrada de {n} é = {res}")
        elif operacao == 7:
            print("Encerrando o programa")
        else:
            print("Operação inválida, escolha uma opção entre 1 à 7")
main()