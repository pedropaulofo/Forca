# coding: utf-8
#menu do jogo

import sys, traceback, forca, rank
from forca import *

global jogador_atual
jogador_atual = "Sem nome"

def inserir_nome():
    print "Digite o nome do jogador:"
    entrada = raw_input()
    if len(entrada) == 0:
        inserir_nome()
    global jogador_atual
    jogador_atual = entrada

def escolher_dificuldade():
	while(True):
		print "Digite o numero correspondente a dificuldade escolhida:\n"
		print "(1) Facil"
		print "(2) Media"
		print "(3) Dificil"
		print "\n(4) Voltar para o menu"

		dificuldades = ["1", "2", "3"]
		opcao = raw_input()
		if opcao == "4":
			main()
				
		if opcao not in dificuldades:
			print "Opcao invalida. Digite apenas um dos numeros indicados.\n"
			continue

		forca.main(opcao, jogador_atual)

def opcao_jogar():
	inserir_nome()
	escolher_dificuldade()
def opcao_ranking():
	rank.main()
def opcao_sair():
	"Saindo do jogo."
	
	sys.exit()

def main():
	opcoes = {"1" : opcao_jogar, "2" : opcao_ranking, "3" : opcao_sair}

	while(True):
		#Instruções de uso:
		print "<<<   JOGO DA FORCA    >>>\n"
		print "Digite o numero correspondente a acao que voce deseja realizar:\n"
		print "(1) Jogar"
		print "(2) Ranking"
		print "(3) Sair\n"
			
		opcao = raw_input()
			
		if opcao not in opcoes.keys():
			print "Opcao invalida. Digite apenas um dos numeros indicados.\n"
			continue
					
		opcoes[opcao]()
