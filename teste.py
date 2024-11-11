import random 

def jogar():
    nivel = 5
    até = nivel
    pontos_valendo = até
    jogando = True
    pontos = 0
    while jogando:
        tentando = True
        tentativas = 0
        n = random.randint(1 , nivel)
        de = 1
        while tentando:
            print('pontuação:',pontos)
            print('Adivinha o número que estou pensando')
            print('de',de,'até',até)
            palpite = int(input('Resposta: '))
            tentativas +=1
            print('tentativas: ',tentativas)
            if palpite == n:
                #usuario acertou
                print('Isso mesmo, você acertou!')
                nivel = nivel*2  # dobra o intervalo de números
                até= nivel
                pontos+=pontos_valendo #soma a pontuação do jogador
                pontos_valendo=até
                tentando = False
                #pergunta se quer parar
                p = input('digite *parar* caso queira finalizar:')
                if p == 'parar':
                    jogando = False
                    adicionar_ao_ranking(pontos)
                    exibir()                 
            else:
                #caso se errou
                pontos_valendo = pontos_valendo/2
                if palpite > n:
                    print('o número que penso é menor')
                    até = palpite-1
                elif palpite<n:
                    print('o número que eu penso é maior')
                    de = palpite + 1

def exibir():
    print('o ranking está feito')
    arquivo = open('nome.txt')
    linhas = arquivo.readlines()
    arquivo.close()
    ranking =[]
    for i in range (0, len(linhas), 2):
        nome = linhas [i] [0:-1]
        pontos = float(linhas[i+1][0:-1])
        ranking.append([pontos,nome])
    ranking = sorted(ranking, reverse=True)
    for x in ranking:
        print(x[0],'_',x[1])
    arq = open('ranking.txt', 'a')
    arq.write(nome + '\n')
    arq.close()

def adicionar_ao_ranking(pontos):
    nome = input("digite o seu nome:")
    arquivo = open('nome.txt','a')
    ranking = []
    nome_pontuacao = [pontos,nome]
    ranking.append(nome_pontuacao)
    arquivo.write(nome+'\n')
    arquivo.write(str (pontos)+'\n')
    arquivo.close()
def palpite(n, pontos):
    if palpite == n:
        #usuario acertou
        print('Isso mesmo, você acertou!')
        nivel = nivel*2  # dobra o intervalo de números
        até= nivel
        pontos +=pontos_valendo #soma a pontuação do jogador
        pontos_valendo=até
        tentando = False
        #pergunta se quer parar
        p = input('digite *parar* caso queira finalizar:')
        if p == 'parar':
            jogando = False
            adicionar_ao_ranking(pontos)
            exibir()                 
    else:
        #caso se errou
        pontos_valendo = pontos_valendo/2
        if palpite > n:
            print('o número que penso é menor')
            até = palpite-1
        elif palpite<n:
            print('o número que eu penso é maior')
            de = palpite + 1
    
jogar()