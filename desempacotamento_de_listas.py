'''
Desempacotamento de listas em python
'''

lista = ['Carolina', 'Inês', 'Maria', 1, 2, 3, 4, 5, 6, 7]

#n1, n2, n3 = lista
n1, n2, n3, *outra_lista, ultimo_da_lista = lista
*outra_lista, n1, n2, n3 = lista

print(ultimo_da_lista)
print(outra_lista)
print(n1, n2, n3)