#Crie uma função que receba como parâmetro um número inteiro. A função deve retornar um número inteiro, conforme a seguir:
#Retornar 1 se o número é positivo
#Retornar -1 se o número é negativo
#Retornar 0 se o número recebido é zero
def inteiros(num):
    if num>0:
        return 1
    elif num<0:
        return -1
    else:
        return 0
def main():
    num=int(input("Escolha um número: "))
    result = inteiros(num)
    print(result)
main()