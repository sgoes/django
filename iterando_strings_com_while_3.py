frase = 'o rato roeu a roupa do rei de roma'
tamanho_frase = len(frase)
contador = 0
nova_string = ''
input_do_usuario = input('Qual a letra que quer colocar maiúscula? ')

while contador < tamanho_frase:
    letra = frase[contador]
    if letra == input_do_usuario:
        nova_string += letra.upper()
    else:
        nova_string += letra
    contador += 1
print(nova_string)