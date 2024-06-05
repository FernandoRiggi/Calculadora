#Faça uma função que calcule o fatorial de um número inteiro postiivo(faça consistencia).
#Transforme seus proframas de consistência de número já implementados para funções
def fatorial(n):
    fat=1
    for numero in n:
        numero=int(n)
    while numero>0:
        fat *=numero
        numero-=1
    return fat
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
    eh_inteiro=inteiro(n)
    if eh_inteiro == True:
        resultadofatorial=fatorial(n)
        print(f"O fatorial de {n} é {resultadofatorial}")
    else:
        print("O número não é inteiro")
main() 