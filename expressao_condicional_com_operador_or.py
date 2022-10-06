# nome = input('Qual o seu nome? ')
# if nome:
#     print(nome)
# else:
#     print('Você não digitou nada ')

# há uma forma muito simples de fazer isto:

# nome = input('Qual o seu nome? ')
# print(nome or 'Você não digitou nada!')

nome = input('Qual o seu nome? ')
print(nome or None or False or 0 or 'Você não digitou nada!')