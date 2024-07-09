from ex115.lib.interface import *
from ex115.lib.arquivo import *
from time import sleep

arq = 'cursoemvideo.txt'

if not arquivoExiste(arq):
    criarArquivo(arq)

#SISTEMA PARA CADASTRO DE PESSOAS

escolha = ''
while True:
    escolha = menu('Sua Opção: ')
    if escolha == 1: #Mostre as pessoas cadastradas
        lerArquivo(arq)
    elif escolha == 2: #Cadastre Novas Pessoas
        cabecalho('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = leiaInt('Idade: ')
        cadastrar(arq, nome, idade)
    elif escolha == 3:
        print('Saindo do sistema...')
        sleep(2)
        print('Volte sempre!')
        break