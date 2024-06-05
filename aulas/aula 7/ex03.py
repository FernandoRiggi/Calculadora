#Elabore a função Real(n) que verifica se ovalor de entrada é um número real e retorna True se verdade e False se falso
def Real(num):
    i=0
    cont=0
    while i < len(num):
        if num[i] =="." or num[i]== ",":
            cont +=1
            i+=1 
        else:
            i+=1
    if cont<=1:
        Real = True
    else:
        Real = False
    return Real
def main():
    num = input("Escolha um número: ")
    nReal= Real(num)
    print(nReal)
main()