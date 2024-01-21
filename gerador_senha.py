from random import choice

letra_min = 'abcdefghijklmnopqrstuvwxyz'
letra_mai = letra_min.upper()
numeros = '0123456789'
especiais = '!@#$%¨&*()-_=+<>,.;[]{}?/'

mapa_caracteres = letra_min + letra_mai + numeros + especiais

senha = ''

def gerarsenha(senha):
    for i in range(9):
        caractere = choice(mapa_caracteres)
        senha += caractere
    return senha

print(gerarsenha(senha))