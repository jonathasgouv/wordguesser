import os
from unicodedata import normalize
import random
import string

# Define a função que retira os acentos das palavras
def remover_pont(txt):
    return txt.translate(str.maketrans('', '', string.punctuation))

def remover_acentos(txt):
    return normalize('NFKD', txt).encode('ASCII', 'ignore').decode('ASCII')

# Retorna uma lista com as letras mais usadas naquela posição, em ordem
def letramusada(lista, pletra):
    pletraordem = []
    pletraordem2 = []
    pl = []

    for n in lista:
        try:
            pl.append(n[pletra - 1])
        except:
            pass

    dict = {}
    for k in pl:
        if k in dict:
            dict[k] += 1
        else:
            dict[k] = 1
    pletraordem2 = (sorted(dict.items(), key=lambda t: t[1], reverse=True))

    for c in pletraordem2:
        pletraordem.append(c[0])

    return pletraordem

# Lê o "banco de dados" que contém as palavras e as armazena na variável "palavras", sem acentos
file = open('palavras.txt')
palavras = file.read().split("\n")

# Armazena a quantidade de letras que a palavra pensada tem
nletras = int(input('Digite o número de letras da palavra (considerando hífen, caso haja) que você pensou, com máximo de 8: '))

# Declara listas que serão usadas em seguida
npalavras = []
palavras2 = []
palavras3 = []
# Armazena todas as palavras que contém a quantidade de letras escolhida anteriormente em uma nova lista chamada "nletras", desconsiderando pontos

for n in palavras:
    if nletras == len(n):
        npalavras.append(remover_acentos(n).lower())

c = 0
n = 0

for k in range(1, nletras + 1):
    ordem = letramusada(npalavras, k)
    cond = 0
    try:
        while cond == 0:
            if  len(npalavras) < 20 and c == 0:
                print("\nHmmm, estou chegando perto!\n")
                c += 1
            if len(npalavras) < 3:
                break
            for c in ordem:
                if c != 0:
                    r = str(input("A {} letra da sua palavra é a letra \"{}\"? [S/N] ".format(k, c))).lower()
                    r = r[0]
                    if r == "s":
                        for n in npalavras:
                            if n[k-1] == c:
                                palavras2.append(n)
                        npalavras.clear()
                        npalavras = palavras2[:]
                        palavras2.clear()
                        ordem.clear()
                        cond += 1
                        break
                    else:
                        for n in npalavras:
                            if n[k-1] != c:
                                palavras2.append(n)
                        npalavras.clear()
                        npalavras = palavras2[:]
                        palavras2.clear()
                        r = 0
                        pass
    except:
        n = 1
        print("\nDesculpe, não achei nenhuma palavra :(")

escolha = random.choice(npalavras)

if n != 0:
    print("\nA palavra que você pensou é: \"{}\"".format(escolha))
