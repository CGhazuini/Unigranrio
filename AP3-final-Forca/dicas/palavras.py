import random


# função para escolher palavra secreta
def sorteiap():
    nrodica = random.randrange(1, 15)  # gerar número aleatório de 1 a 15
    arquivo = open('dicas/palavras-dicas.txt', 'r')
    dados = list()

    # procurar número randômico gerado no arquivo da variável 'arquivo'
    for linha in arquivo:
        vlista = linha.split('|')
        dados.append(vlista)

        for x in range(0, len(dados)):
            vnrdica = int(dados[x][0])
            if vnrdica == nrodica:
                vpalavra = dados[x][1]
                vdica = dados[x][2]
    # fecha arquivo
    arquivo.close()

    # jogar palavra e dica encontrada no arquivo.txt para a variável vretorno
    vretorno = vpalavra + '|' + vdica

    return vretorno