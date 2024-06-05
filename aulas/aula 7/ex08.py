#Faça uma função que retorne a sequencia de Fibonacci recebendo
#como parâmetro o número (faça a consistência) de termos desejado.
def fibonacci(n):
    for numero in n:
        numero = int(n)
    fibonacci=0
    n1=1
    i=0
    while i<numero:
        print(f"{fibonacci}", end=" ")
        n2=fibonacci
        fibonacci+=n1
        n1=n2
        i+=1
    return fibonacci
def inteiro(n):
    i=0
    inteiro=True
    while i < len(n) and inteiro==True:   
        if n[i] != "," and n[i]!= ".":
            inteiro = True
            i+=1
        else:
            inteiro = False
        return inteiro
def main():
    n=input("Escolha um número: ")
    result_int=inteiro(n)
    if result_int==True:
        resultfibonacci=fibonacci(n)
        print(resultfibonacci)
    else:
        print("Número não é inteiro")
main()