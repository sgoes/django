l1 = [1, 2, 3]
l2 = [4, 5, 6]
# l3 = l1 + l2  # aqui estou a concatenar as listas
l1.extend(l2)  # l1 extendeu à l2
l1.extend('a')  # também serve para adicionar valores ao final da lista
l2.append('b')  # normalmente quando quero adicionar valores à minha lista utilizo o append
l2.insert(0, 'banana')  # serve para inserir um valor na lista na posição que preferir
print(l2)
l2.pop()  # serve para remover um valor da lista

print(l1)
print(l2)
# print(l3)
#     0  1  2  3  4  5  6  7  8
l4 = [1, 2, 3, 4, 5, 6, 7, 8, 9]

del(l4[3:5])  # eliminar valores dentro da lista com marcador de ínicio e fim, o valor do último índice não é removido
print(l4)

l4.insert(0, 'Banana')  # aqui estou a inserir 'Banana' ao indice 0 da lista4
print(l4)
del(l4[0])  # aqui estou a remover o índice 0 da lista4
print(l4)


# Nós também conseguimos pegar o valor máximo e o mínimo da nossa lista
print(max(l4))
print(min(l4))
print('#########################')
# range  porém o python tem uma funcao chamada list, funcao builtin que permite tornar um objeto interável em uma lista
l5 = list(range(0, 10))  # isto é bom para criar lista logo de caras
print(l5)
print('################################')
for valor in l5:
    if valor % 8 == 0:
        print(valor)

print('############################')
l6 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
soma = 0
for valor in l6:
    soma += valor
    print(f'{soma} + {valor} = {soma}')
print(soma)


