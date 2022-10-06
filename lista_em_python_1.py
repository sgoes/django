'''
Listas em Python
-fatiamento
-append, insert, pop, del, clear, extend
min, max
range
'''

#         0    1    2    3    4     5
lista = ['A', 'B', 'C', 'D', 'E', 10.5]
#     -   6    5    4    3    2     1
#lista[5] = 'Qualquer outra coisa'  # alterar o valor de um elemento da lista
print(lista[5])

# se eu quiser apenas ver os três primeiros valores da lista:
print(lista[0:3])
print(lista[:4:2])  # mostra a lista a iniciar do indice 0 ao indice 4 de 2 em 2
print(lista[:3])  # mostra o valor até ao índice 2, o último valor não é mostrado
print(lista[2:])  # aqui revela do índice que quero que inicie até ao final da lista
print(lista[-1])  # serve para encontrar o último valor do índice da lista
print(lista[::2])  # o começo estou a omitir, o fim tbm estou a omitir então é até ao final da lista, pulando de 2 em 2
print(lista[::-1])  # aqui estou a inverter a minha lista
