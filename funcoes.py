"""
Funções - def em Python (Parte 1)
"""


def saudacao(msg='Olá', nome='usuário'):
    nome = nome.replace('i', '1')
    msg = msg.replace('i', '1')
    # print(msg, nome)
    return f'{msg} {nome}'
variavel = saudacao()
print(variavel)
# saudacao(nome='Carolina', msg='Hi,')
