"""
1 - Crie uma função que exibe uma saudacao com os parâmetros saudacao nome.
"""


def saudacao(msg='Olá', nome=input('Qual o seu nome: ')):
    return f'{msg}, {nome}'

variavel = saudacao()
print(variavel)

"""
2 - Crie uma função que recebe 3 números como parâmetros e exiba a soma entre eles
"""

def soma(n1,n2,n3):
    print(n1+n2+n3)
soma(2,3,4)

"""
3- Crie uma função que receba 2 números. O primeiro é um valor e o segundo um percentual (ex.10%). Return o valor do primeiro número somado do aumento do percentual do mesmo.
"""

def aumento_percentual(valor, percentual):
    return valor + (valor * percentual / 100)


ap = aumento_percentual(50, 10)
print(ap)
ap = aumento_percentual(100, 10)
print(ap)
ap = aumento_percentual(10, 10)
print(ap)
ap = aumento_percentual(15, 100)
print(ap)

"""4 - Fizz Buzz - Se o parâmetro da função for divisivel por 3 ,retorne fizz, se o parâmetro da função for divisivel 
por 5, retorne buzz. Se o parâmetro da função for divisível por 5 e por 3, retorne FizzBuzz, caso contrário retorne o 
número enviado """


def fb(n):
    if n % 3 == 0 and n % 5 == 0:
        return f'FIZZBUZZ, {n} é divisivel por 3 e 5'
    if n % 3 == 0:
        return f'FIZZ, {n} é divisivel por 3'
    if n % 5 == 0:
        return f'BUZZ, {n} é divisivel por 5'
    return f'{n} --> não é divisivel nem por 3 e 5'


from random import randint

for i in range(10):
    aleatorio = randint(0, 10)
    print(fb(aleatorio))
