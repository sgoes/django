"""
For in Python
Iterando strings com for
Funçao range(start = 0, stop, step = 1=
"""
# texto = "Python"
# contador = 0
# while contador < len(texto):
#     print(texto[contador])
#     contador += 1

# texto = 'Python'
#
# for letra in texto:
#     print(letra)

# texto = 'Python'
# for n, letra in enumerate(texto):
#     print(n,letra)

# for n in range(0, 100, 7):
#     print(n)

# No seguinte exemplo será executado um laço FOR que irá permitir transformar duas letras da string inserida em letras maiusculas.
texto = 'python'
nova_string = ''

# for letra in texto:
#     if letra == 't':
#         nova_string = nova_string + letra.upper()
#     elif letra == 'h':
#         nova_string = nova_string + letra.upper()
#     else:
#         nova_string += letra
# print(nova_string)
#############################################

# Ainda posso usar as palavras reservadas CONTINUE e BREAK por exemplo se quiser que uma letra não apareça na minha nova palavra descrevo da seguinte forma o laço:
letra_usuario = input('Insira uma palavra: ')

for letra in letra_usuario:
    if letra == '':
        continue
    elif letra == '':
        nova_string += letra.upper()
    else:
        nova_string += letra
print(nova_string)

