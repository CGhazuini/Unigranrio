
# função para imprimir linhas
def lin(tam = 50):
    return'\033[33m-\033[m' * tam

# função para inserir um título pro jogo
def título(txt):
    print(lin())
    print(txt.center(60))
    print(lin())