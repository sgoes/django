

# vamos imaginar que temos um sistema de login e vamos verificar se o usuario está logado
# logged_user = False
# if logged_user:
#     msg = 'Usuário logado'
# else:
#     msg = 'Usuário precisa logar'
# print(msg)

# ainda posso encurtar isto atraves do operador ternario
# logged_user = True # or False
# msg = 'Usuário logado.' if logged_user else 'usuario precisa logar '
# print(msg)

# Imaginando que tenho um sistema para maiores de 18 anos de idade
# idade = 18
# if idade >= 18:
#     print('Pode acessar')
# else:
#     print('Não pode acessar')

# idade = 17
# e_de_maior = (idade >= 18)
# msg = 'Pode acessar' if e_de_maior else 'Não pode acessar'
# print(msg)
'''
Operador ternario em Python
'''

idade = input('Qual a sua idade? ')
if not idade.isnumeric():
    print('Digite um número')
else:
    idade = int(idade)
    e_de_maior = (idade >= 18)
    msg = 'Pode acessar' if e_de_maior else 'nao pode acessar'
print(msg)