#1 -Crie as perguntas e respostas do seu jogo em um arquivo. Faça seu jogo lê-las assim que começa.
#2 -Faça com que seu jogo funcione em um loop infinito.
# Toda vez que uma partida acaba, outra começa logo em seguida. Agora faça seu jogo registrar
# o placar e o nome de cada jogador em um arquivo.
#3 -Modifique novamente o jogo para que, dessa vez, ao final de uma partida.
# mostre apenas os nomes e placares dos dez melhores resultados, se houver.
#  Os nomes e placares devem ser listados em ordem decrescente de placar.
#4 -Faça com que seu jogo escolha aleatoriamente apenas um número N de perguntas,
# lido a partir da primeira linha do arquivo de perguntas e mostre apenas essas perguntas.

# A cada partida, as perguntas devem ser sorteadas novamente.
# Seu jogo não deve considerar a mesma pergunta duas vezes
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

listaIndicesPerguntas = [i for i in range(1,14)]
#--------------------------------------------------------------------------------------------------------------------------------------------------------#
#Cadastro de jogadores.
def cadastroDeJogadores():
    global nomeDojogador
    while True:
        nomeDojogador = (input("Informe seu nome: "))
        if nomeDojogador == '':
            print('================================')
            print('  Informação inválida\nDigite algum nome para se cadastrar no jogo')
            print('================================')
            continue
        else:
            print(f'Jogador {nomeDojogador} cadastrado!')
            print('--------------Star--------------------', flush=True)
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
                    sleep(2)
                    print("Parabéns!")
                    pontos = pontos + 667
                    print("Sua pontuação é de {}".format(pontos), flush=True)
                    sleep(3)
                    break
                elif resp not in alternativas:
                    print('##################################################################')
                    print('Resposta inválida. Digite uma opção correspondente as alternativas')
                    print('##################################################################')
                    continue
                else:
                    sleep(1)
                    print("Resposta incorreta!")
                    print("Infelizmente Não Foi Dessa Vez, Tente Novamente Mais Tarde. Não Desista!")
                    break

            limparLista()

menu()

print("----"*20)
print("Sua pontuação foi : " , (pontos))
salvarNoRanking()
exibirRanking()