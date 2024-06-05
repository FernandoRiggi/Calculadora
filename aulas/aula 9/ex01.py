def ler_dados_arquivo(nome):
    ref_arq= open(nome, 'r')
    lista=[]
    for linha in ref_arq:
        lista.append(linha)
    return lista
def quantidade_notas(lista):
    for linha in lista:
        linha=linha.split()
        print(f"Nome:{linha[0]} {len(linha)-1}")
def mais_que_6_notas(lista):
    print("Alunos com mais que 6 notas:",end=" ")
    for linha in lista:
        linha=linha.split()
        if len(linha)-1 > 6:
            print(f"{linha[0]}")
def média(lista):
    for linha in lista:
        linha=linha.split()
        média=0
        i=1
        while i < len(linha):
            nota = int(linha[i])
            média += nota
            i+=1
        média = média/len(linha)-1
        print(f"Nome:{linha[0]} Média:{média:.2f}")
def minmáx(lista):
    for linha in lista:
        linha=linha.split()
        notas=[]
        i=1
        while i < len(linha):
            nota = int(linha[i])
            notas.append(nota)
            i+=1
        i=0
        min=notas[i]
        max=notas[i]
        while i < len(notas):
            if min > notas[i]:
                min = notas[i]
            elif max < notas[i]:
                max=notas[i]
            i+=1
        print(f"Nome: {linha[0]}, Maior nota: {max}, Menor nota: {min}")    
def main():
    nome_arq = './estudantes.txt'
    dados_arquivos= ler_dados_arquivo(nome_arq)
    quantidade_notas(dados_arquivos)
    mais_que_6_notas(dados_arquivos)
    média(dados_arquivos)
    minmáx(dados_arquivos)
main()
