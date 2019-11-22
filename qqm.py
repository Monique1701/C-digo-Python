import random
from time import sleep

print("------*"*31)
print ("Vem brincar! Vem Curtir! Vem testar seu conhecimentos!")
print("------*"*31)




print("Divirta-se na brincadeira do 'Quem quer ser um miliónario' ?")
pontos = 0
lista = []
pontos = 0
nomeDojogador = ''

listaIndicesPerguntas = [i for i in range(1,16)]
#--------------------------------------------------------------------------------------------------------------------------------------------------------#
#Cadastro de jogadores.
def cadastroDeJogadores():
    global nomeDojogador
    while True:
        nomeDojogador = (input("Informe seu nome: "))
        nomeDojogador = nomeDojogador.replace(' ','')
        if nomeDojogador == '':
            print('================================')
            print('  Informação inválida\nDigite algum nome para se cadastrar no jogo')
            print('================================')
            continue
        else:
            print('Jogador {} cadastrado!'.format(nomeDojogador))
            print('--------------Play--------------------', flush=True)
            sleep(2)
            break
#---------------------------------------------------------------------------------------------------------------------------------------------------------#
#Salvando os nomes do jogadores e seus repectivos pontos em um arquivo.
def salvarNoRanking():
    ranking = open("ranking.txt", 'a')
    ranking.write("{} {}.\n".format(pontos, nomeDojogador))
    ranking.close()
#----------------------------------------------------------------------------------------------------------------------------------------------------------#
#Exibindo o ranking.
def exibirRanking():
    lista = []
    listaTuplas = []

    ranking = open("ranking.txt", 'r')

    fim = 0
    for i in ranking:
        lista.append(i)

    for i in lista:
        for pos, elemento in enumerate(i):
            if elemento == ' ':
                fim = pos            
                
        #pegar o valor
        pontosR = ''
        nomeR = ''

        for j in range(fim):
            pontosR += i[j]

        for j in range(fim, len(i)):
            nomeR += i[j]

        valores = (int(pontosR), nomeR)
        listaTuplas.append(valores)

    newLista = sorted(listaTuplas, reverse=True)

    print("--------------------------Ranking----------------------------------")

    for i in newLista:
        print('Pontos: {} --- Nome: {}'.format(i[0], i[1]))
#-------------------------------------------------------------------------------------------------------------------------------------------------------------#
#Função que abre o arquivo para a leitura e Varre o conteúdo do arquivo e Colocar em uma lista.
def getPerguntas():

    if len(listaIndicesPerguntas) == 0:
        print('--------------------------------------- O JOGO ACABOU ---------------------------------------')
    else:
        indice = random.choice(listaIndicesPerguntas)
        listaIndicesPerguntas.remove(indice)

        arq = open('pergunta{}.txt'.format(indice),'r')

        for i in arq:
            lista.append(i)
#
def limparLista():
    lista.clear()

#Nessa função contém o menu onde o jogador está interagindo 
def menu():
    global pontos
    
    cadastroDeJogadores()
    resposta = (input("Deseja começar? [S/N]: "))
    print('----'*35)
        
    if resposta.lower() == 'n':
        pass
    
    else:
        for i in range(1,15):
            getPerguntas()        

            print(lista[0])
            print(lista[1])
            print(lista[2])
            print(lista[3])
            print(lista[4])
            
            #Bloco aonde eu comparo as repostas
            while True:
                alternativas = ['a', 'b', 'c', 'd']
                resp = (input("{} - Qual a alternativa correta? ".format(i)))
                
                respCorreta = lista[5]
                
                if resp.lower() == respCorreta:
                    print("PROCESSSANDO.......")
                    sleep(0)
                    print("Parabéns!")
                    pontos = pontos + 100000
                    print("Sua pontuação é de {}".format(pontos), flush=True)
                    print("---------------------------------------------*-------------------------------------------------")
                    sleep(1)
                    break
                elif resp not in alternativas:
                    print("------------------------------------------------------------------------------------------------")
                    print('##################################################################')
                    print('Resposta inválida. Digite uma opção correspondente as alternativas') #Tratamento de erros
                    print('##################################################################')
                    continue
                else:
                    sleep(0)
                    print("Resposta incorreta!")
                    print("Infelizmente Não Foi Dessa Vez, Tente Novamente Mais Tarde. Não Desista!")
                    print('-------------------------------------------------------------------------------------------------')
                    break

            limparLista()

menu()

print("----"*20)
print("Sua pontuação foi : " , (pontos))
salvarNoRanking()
exibirRanking()
