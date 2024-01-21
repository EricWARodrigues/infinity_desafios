from random import choice

letra_min = 'abcdefghijklmnopqrstuvwxyz'
letra_mai = letra_min.upper()
numeros = '0123456789'
especiais = '!@#$%¨&*()-_=+<>,.;[]{}?/'

mapa_caracteres = letra_min + letra_mai + numeros + especiais

senha = ''

def gerarsenha(letra, senha):
    senha += letra
    for i in range(9):
        caractere = choice(mapa_caracteres)
        senha += caractere
    return senha

print('-' * 30)
print('Bem vindo ao gerador de SENHA')
print('-' * 30)

nome = input('\nInforme seu nome: ')
primeira_letra = nome[0]
print(f'\nGeramos a senha "{gerarsenha(primeira_letra, senha)}"')
