#Faça uma função que receba quatro valores, referente as ntas que um aluno obteve nos bimestres.
#A função deve retornar True se o aluno foi aprovado e False caso contrário
import math
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
def media(valores):
    media=0
    for nota in valores:
        media+=float(nota)
    media = media/len(valores)
    return math.ceil(media)    
def aprovado(média):
    if média >=6:
        return True
    else:
        return False
def main():
    i=0
    valores=[]
    while i<4:
        num = input("Escolha um número: ")
        nReal= Real(num)
        if nReal == True:
            i+=1
            valores.append(num)
    média = media(valores)
    print(f"{aprovado(média)}")    
main()