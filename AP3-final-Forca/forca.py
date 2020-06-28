"""
UNIVERSIDADE UNIGRANRIO
AVALIAÇÃO AP3 - PRÁTICA DE PROGRAMAÇÃO EM SISTEMAS DE INFORMAÇÃO
ALUNO = ANTONIO CELIO SILVA GHAZUINI (5405625)
PROJETO JOGO DA FORCA EM PYTHON
"""

from interface.forca import forca
from interface.abertura import título
from dicas.palavras import sorteiap


título('\033[31m"Bem vindo ao JOGO DA FORCA"\033[m')
jogador = input(str('\033[33mDigite seu Nome: \033[m'))  # Guardar o nome do jogador em uma variável


continuar = 'S'
partidas=vitorias=derrotas = 0  # Armazenar o número de partidas, vitórias e derrotas e inserir 0 como default


while continuar in 'Ss':

    # Incrementar o número de partidas em +1
    erros=0
    partidas +=1

    # Sortear palavra secreta e dica
    lletras = list()
    dadospalavra = list()  # Lista - palavra sorteada
    listasorteio = sorteiap()  # Gerar a palavra e dica aleatória
    vlistap = listasorteio.split('|')  # Dividir string recebida
    dadospalavra.append(vlistap)  # Incluir string em uma lista para recuperar os dados

    for x in range(0,len(dadospalavra)):
        word = dadospalavra[x][0]  # Recuperar palavra
        dicauser = dadospalavra[x][1]  # Recuperar dica

    temp=[]

    for letra in word:
        temp.append('_')

    while True:


        print('\n'*20)
        forca(erros, jogador)   # Imprimir o desenho da forca

        # Imprimir a dica
        print(f'Dica: \033[33m{dicauser}\033[m')

        # Imprimir a palavra secreta
        print('\n\n\033[33mPalavra Secreta:\033[m ', end='')

        for let in temp:
            print(let, end=' ')
        print('\n'*2)

        # Verificar se o jogador perdeu
        if erros==6:
            derrotas +=1  # Incrementar o número de derrotas em +1
            print(f'\n Lamento! \033[31m{jogador}\033[m, VOCÊ PERDEU! \033[31m Foi enforcado!!!\033[m')
            print('')
            print(f'\033[51mTotal Partidas:\033[m {partidas}')
            print(f'\033[36mTotal Vitórias:\033[m {vitorias}')
            print(f'\033[31mTotal Derrotas:\033[m {derrotas}')
            print('\n'*2)
            continuar = str(input('Você quer jogar novamente? [S/N] : ')).upper().strip()[0]
            break  # Sair do jogo

        # Verificar se o jogador ganhou
        ganhouJogo=True
        for let in temp:
            if let=='_':
                ganhouJogo=False

        if ganhouJogo:
            vitorias +=1    # Acrescentar mais 1 ao número de vitórias
            print(f'\n PARABÉNS \033[36m{jogador}\033[m, VOCE ACERTOU!!!')
            print('')

            print(f'\033[51mTotal de  Partidas:\033[m {partidas}')
            print(f'\033[36mNúmero de Vitórias:\033[m {vitorias}')
            print(f'\033[31mNúmero de Derrotas:\033[m {derrotas}')
            print('\n'*2)
            continuar = str(input('Jogar Novamente? [S/N] : ')).upper().strip()[0]

            break

        # Capturar a letra digitada pelo usuario
        print(f'\033[31mLETRAS JÁ DIGITADAS:\033[m')
        print(lletras)
        letraDig=input("Digite uma letra: ")
        letraDig = letraDig.upper()     #Deixar a letra maiúscula
        lletras.append(letraDig)

        # Verificar se o jogador acertou alguma letra
        errouLetra=True
        for i, let in enumerate(word):
            if word[i]==letraDig:
                temp[i]=word[i]
                errouLetra=False
        if errouLetra:
            erros=erros+1


