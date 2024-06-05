#A seguinte tabela contém tradução de algumas palavras em inglês para a língua dos piratas.
#Escreva um programa que pergunta ao usuário uma frase em inglês e imprime a tradução da frase para a língua
#dos piratas.
ing_pir={}
ing_pir['sir']='matey'
ing_pir['hotel']='fleabag inn'
ing_pir['student']='swabbie'
ing_pir['boy']='matey'
ing_pir['madam']='proud beauty'
ing_pir['professor']='foul blaggart'
ing_pir['restaurant']='galley'
ing_pir['your']='yer'
ing_pir['excuse']='arr'
ing_pir['students']='swabbies'
ing_pir['are']='be'
ing_pir['lawyer']='foul blaggart'
ing_pir['the']='th'
ing_pir['restroom']='head'
ing_pir['my']='me'
ing_pir['hello']='avast'
ing_pir['is']='be'
ing_pir['man']='matey'
frase=input("Crie uma frase em ingles: ")
palavras=frase.split()
traducao=[]
for palavra in palavras:
    if palavra in ing_pir:
        traducao.append(ing_pir[palavra])
    else:
        traducao.append(palavra)
frase_traduzida=' '.join(traducao)
print(f"Frase em inglês original: {frase}")
print(f"Frase traduzida para pirata: {frase_traduzida}")