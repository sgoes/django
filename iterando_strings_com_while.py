#        Índices --> se cada elemento tem indices é sinal que é interável
#        0123456789


frase = 'o rato roeu a roupa do rei de roma'
tamanho_frase = len(frase)
contador = 0
nova_string = ''

while contador < tamanho_frase:
    nova_string += frase[contador]
    contador += 1
    print(nova_string)
