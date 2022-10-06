"""
Split, Join, Enumerate em Python
* Split - Dividir uma string
* Join - Juntar uma lista #str
* Enumerate - Enumerar elementos da lista # list --> para objetos iteraveis
"""

string = "O Brasil é o país do futebol, o Brasil é penta"
lista_1 = string.split(' ')
lista_2 = string.split(',')

print(lista_1)
print(lista_2)

# se quiser interar sobre a lista
for valor in lista_1:
    print(valor)
print('####################################################################')
# contar palavras dentro de um determinada lista
for valor in lista_1:
    print(f'A palavra "{valor}" apareceu {lista_1.count(valor)}x na frase.')



print("######################################################################")

# Fazer a contagem da palavra que apareceu mais vezes na string
palavra = ''
contagem = 0
for valor in lista_1:
    qtd_vezes = lista_1.count(valor)

    if qtd_vezes > contagem:
        contagem = qtd_vezes
        palavra = valor
print(f'A palavra que apareceu mais vezes é "{palavra}" ({contagem}x)')