# coding: utf-8
import random, sys, menu

def separa_palavra(palavra):
    letras = []
    for letra in palavra:
        letras.append(letra)
    return letras

def nao_ganhou(acertos):
    for letra in acertos:
        if letra == False:
            return True
    return False

def exibe_forca(chances):
    altura_vazia = "|       "
    print "________"
    #cabeca
    if chances == 5:
        print altura_vazia
    else:
        print "|     O "
    #troco + braços
    if chances >= 4:
        print altura_vazia
    elif chances >=3:
        print "|    /| "
    else:
        print "|    /|)"
    #pernas
    if chances >=2:
        print altura_vazia
    elif chances == 1:
        print "|    /  "
    else:
        print "|    /) "
    print altura_vazia
    print altura_vazia + "\n"

def mostra_palavra(palavra, acertos):
    exibida = ""
    for i, letra in enumerate(palavra):
        if acertos[i]:
            exibida += letra
        else:
            exibida +="_"
        exibida += " "
    print exibida

def salva_jogador_pontuacao(nome, pontuacao):
    arquivo = open("ranking.txt", "r")
    atual = arquivo.read()
    arquivo.close()
    arquivo = open("ranking.txt", "w")
    arquivo.write(atual)
    arquivo.write("Jogador: " + nome + " Chances restantes: " + str(pontuacao) + "#")
    arquivo.close()


def fim_partida(opcao, jogador):
    print "O que voce deseja fazer:"
    print "(1) Jogar novamente"
    print "(2) Mudar dificuldade"
    print "(3) Voltar ao menu"
    print "(4) Fechar"
    print "Digite o numero correspondente a dificuldade escolhida:\n"

    opcao = raw_input()

    if opcao== "1":
        main(opcao, jogador)
    elif opcao == "2":
        menu.escolher_dificuldade()
    elif opcao == "3":
        menu.main()
    elif opcao == "4":
        sys.exit()
    else:
        fim_partida(opcao, jogador)


faceis = ["casa", "gato", "chocolate", "pizza"]
medias = ["casa", "gato", "chocolate", "pizza"]
dificeis = ["casa", "gato", "chocolate", "pizza"]
global palavras_dif
palavras_dif = {"Facil" : faceis, "Medio" : medias, "Dificil" : dificeis}

def main(opcao, jogador):
    dificuldade = {"1" : "Facil", "2" : "Medio", "3" : "Dificil"}
    print "Partida inciada! Dificuldade: " + dificuldade[opcao] + "\n"

    palavras = palavras_dif[dificuldade[opcao]]
    palavra = separa_palavra(palavras[random.randint(0,len(palavras)-1)])
    acertos = []
    chances = 5

    for i in enumerate(palavra):
        acertos.append(False)

    print
    print "A palavra tem " + str(len(palavra)) +" letras"

    while(nao_ganhou(acertos)):
        exibe_forca(chances)
        mostra_palavra(palavra, acertos)

        if chances == 0:
            print "Voce perdeu. A palavra era: " + "".join(palavra)
            break

        print "Voce tem " + str(chances) + " chance(s)"
        print "Digite a letra que voce quer arriscar, ou:"
        print "(1) Chutar palavra"
        print "(2) Desistir"

        tentativa = raw_input()

        if len(tentativa) != 1:
            print "Tentativa invalida. Digite apenas a letra que voce arrisca."
            continue

        elif tentativa == "1":
            print "Digite a palavra que voce deseja arriscar"
            chute = raw_input().upper()
            if chute == "".join(palavra).upper():
                for letra in acertos:
                    letra = True
                break
            else:
                chances -= 1
                print "Chute incorreto."
                continue

        elif tentativa == "2":
            print "Fim da partida"
            fim_partida(opcao, jogador)

        letraErrada = True
        for letra in range(len(palavra) ):
            if palavra[letra] == tentativa:
                acertos[letra] = True
                letraErrada = False

        if letraErrada:
            chances -= 1
            print "Errou! " + tentativa + " nao esta na palavra. Voce perdeu uma chance."
            print



    if chances > 0:
        mostra_palavra(palavra, acertos)
        print "Parabens, " + jogador + "! Voce acertou com " + str(chances) + " restantes."
        salva_jogador_pontuacao(jogador, chances)
    fim_partida(opcao, jogador)
