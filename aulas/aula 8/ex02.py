#Elabore um programa para armazenar uma agenda de telefones em um dicionário. Cada pessoa pode ter um ou mais telefones e a chave do
#dicionário é o nome da pessoa. O programa deve ter as seguintes funções:
#a) incluirNovoNome() – essa função acrescenta um novo nome na agenda, com um ou mais telefones. Ela deve receber como argumentos o
#nome e os telefones;
#b) incluirTelefone() – essa função acrescenta um telefone em um nome existente na agenda. Caso o nome não exista na agenda, você deve
#perguntar se a pessoa deseja incluí-lo. Caso a resposta seja afirmativa, use a função anterior para incluir o novo nome;
#c) excluirTelefone() – essa função exclui um telefone de uma pessoa que já está na agenda. Se a pessoa tiver apenas um telefone, ela deve ser
#excluída da agenda;
#d)excluirNome() – essa função exclui uma pessoa da agenda.
#e)consultarTelefone – essa função retorna os telefones de uma pessoa na agenda.
def novonome(nome,telefones, AGENDA): # função para adicionar um nome na agenda
    if nome.lower() not in AGENDA:
        AGENDA[nome.lower()]=telefones
        return True
    else:
        return False
def novotelefone(nome, telefone , AGENDA): #função para adicionar um novo telefone
    if nome.lower() in AGENDA:
        AGENDA[nome.lower()].append(telefone) 
        return True
    else:
        return False
def removetelefone(nome,telefone,AGENDA): #função para remover um telefone
    if nome.lower() in AGENDA:
        for i in range(len(AGENDA[nome.lower()])):
            if telefone == AGENDA[nome.lower()][i]:
                del AGENDA[nome.lower()][i]
                return True
            else:
                return False
    else:
        print("Usuário não encontrado")
def removenome(nome, AGENDA): #função para remover um nome da agenda
    if nome.lower() in AGENDA:
        del AGENDA[nome.lower()]
        return True
    else:
        return False
def conuslutartelefone(nome,AGENDA): #função para consultar os telefones de um nome
    if nome.lower() in AGENDA:
        return True
    else:
        return False
def menu():
    print("Escolha uma opção de 1 à 5 ou digite 6 para sair")
    print("1. Incluir novo nome na lista")
    print("2. Incluir novo telefone na lista")
    print("3. Excluir telefone da lista")
    print("4. Excluir Nome da lista")
    print("5. Consultar telefones do nome")
    print("6. Sair")
    operacao = int(input("Escolha uma opção de 1 à 5 ou digite 6 para sair: "))
    return operacao
def main():
    operacao=1
    AGENDA={}
    while operacao != 6:
        operacao = menu() #mostrar o menu
        if operacao == 1:
            nome=input("Digite seu nome: ")
            valortelefone=int(input("Digite quantos telefones deseja adicionar: "))
            telefones=[]
            for i in range(valortelefone):
                telefones.append(input(f"Digite o telefone {i+1}: "))
            funcao1=novonome(nome, telefones, AGENDA, valortelefone)
            if funcao1 == True:
                print("O nome e o(s) telefone(s) foi adicionado a lista")
            else:
                print("O nome já existe na lista")
        elif operacao ==2: 
            nome = input("Digite seu nome: ")
            telefone=input("Digite seu telefone: ")
            funcao2=novotelefone(nome, telefone, AGENDA) 
            if funcao2 == True:
                print("O telefone foi adicionado")
            else:
                print("Usuário não encontrado, para adicionar escolha a opção 1 no menu")
        elif operacao==3:
            nome= input("Digite seu nome: ")
            telefone=input("Digite o telefone que deseja excluir: ")            
            funcao3=removetelefone(nome,telefone,AGENDA)
            if funcao3 == True:
                print(f"O telefone foi removido da lista")
            else:
                print("O telefone não foi encontrado na lista")
        elif operacao==4:
            nome=input("Digite o nome que deseja remover: ")
            funcao4=removenome(nome,AGENDA)
            if funcao4==True:
                print("Usuário deletado")
            else:
                print("Usuário não encontrado")
        elif operacao==5:
            nome=input("Digite o nome que deseja consultar: ")
            funcao5=conuslutartelefone(nome,AGENDA)                
            if funcao5==True:
                print(f"Os telefones de {nome} são {AGENDA[nome.lower()]}")
            else:
                print("Usuário não encontrado")
        elif operacao==6:
            print("Encerrando programa")
        else: 
            print("Operação inválida, escolha uma opcção entre 1 à 6")
main()