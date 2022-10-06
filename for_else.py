"""
For/ Else em Python
"""

# for valor in variavel:
#     print(valor)
#     # continue
#     # break
#     print(valor)

# name = 'carolina'.capitalize()
# print(name)
# print('Hello %s' %name)
#
# num = 5
# print('I have %x aple' % num)


# for valor in variavel:
#     if valor.startswith('A'):
#         print('Começa com "A"', valor)
#     else:
#         print("Não começa com 'A'", valor)


# comeca_com_a = False
# for valor in variavel:
#     if valor.lower().startswith('a'):
#         comeca_com_a = True
#
# if comeca_com_a:
#     print('Existe uma palavra que começa com A')
# else:
#     print('Não existe uma palavra que começa com A ')

# print(r"Hello there!\nHow are you?\nI\'m doing fine.")
# print("Hello there!\nHow are you?\nI\'m doing fine.")


variavel = ['Carolina', 'Inês', 'Afonso']
for valor in variavel:
    if valor.lower().startswith('a'):
        continue
    print(valor)
else:
    print('O nome %s, começa com A' % valor)
