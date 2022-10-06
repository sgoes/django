"""
CPF = 168.995.350 -09
---------------------------------------------------------------
1 * 10 = 10                 #   1 * 11 = 11
6 * 9 = 54                  #   6 * 10 = 60
8 * 8 = 64                  #   8 * 9 = 72
9 * 7 = 63                  #   9 * 8 = 72
9 * 6 = 54                  #   9 * 7 = 63
5 * 5 = 25                  #   5 * 6 = 30
3 * 4 = 12                  #   3 * 5 = 15
5 * 3 = 15                  #   5 * 4 = 20
0 * 2 = 0                   #   0 * 3 = 0
                            #   0 * 2 = 0
                            #
       297                  #           343
11 - (297 % 11) = 11        #       11 - (343 % 11) = 9
11 > 9 = 0                  #
Digito 1 = 0                #   Digito 2 = 9
"""

# Vou pegar os primeiros digitos do CPF e multiplicar por uma contagem regressiva de 10 a 2, depois vou pegar o resultado das multiplicações e somar. Depois faço o calculo que está em baixo

# primeiro vou pegar no CPF e colocá-lo em string
cpf = '16899535009'
# o novo CPF é igual aos primeiros digitos
novo_cpf = cpf[:-2]
print(novo_cpf)
# agora eu quero fazer apenas num loop único todo este cálculo
reverso = 10
cpf = '16899535009'
novo_cpf = cpf[:-2]
print(novo_cpf)

cpf = '16899535009'
novo_cpf = cpf[:-2]
print(novo_cpf)

for index in range(19):
    print('o index é', index)
    if index > 8:
        index -= 9
