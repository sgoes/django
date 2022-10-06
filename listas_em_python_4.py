"""
Listas em Python
append, insert, pop, del, clear, extend, +
min, max
range
"""
# palavra secreta de jogo

# a próxima lista serve para armazenar a letras digitadas pelo usuário vou iniciar o jogo a partir de um laço While
# True, de seguida vou pedir para o usuário digitar uma letra. Após isso vou checkar se o usuário digitou mais que
# uma letra a partir da função len, se se letra digitada for maior que um, mando uma mensagem a dizer que o usurario
# apenas pode escrever uma letra e dou um continue. Agora quero que a letra digitada fique indexada à minha lista de
# digitadas[], para isso vou recorrer à função .append(letra). Agora vou verificar se a letra digitada pelo usuario
# encontra-se dentro da palavra secreta, crio então uma estrutura de decisão para tal, se a letra digitada estiver em
# secreto, envio uma mensagem ao usuário a informar que a letra digitada encontra-se na palavra secreta,
# caso contrário informo que a letra digitada não se encontra e automaticamente também removo esta letra à lista de
# digitadas através da função .pop(). Após esta verificação preciso de criar um mecanismo que revele quais as letras
# digitadas que o usuario acertou e ao mesmo tempo mostre as outras que faltam revelando um *, para isto preciso de
# declarar uma nova variável que vai receber as letras digitadas, crio assim um laço FOR que vai percorrer a palavra
# secreta e indicar-me se a letra digitada está certa se sim, adicionamos esta letra a nova ao secreto_temporario,
# caso contrario adicionamos um * à palavra secreta_temporaria. Por ultimo, criamos uma estrutura de decisão que nos
# vai reveler se o secreto_temporario == secreto e se assim o for terminamos o jogo com um break, caso contrario
# mostramos como está o secreto_temporario. Ainda posso colocar quantas vezes o usuário pode tentar acertar a palavra, declaro uma variável no inicio "chances" e o numero de vezes que o usurario pode tentar, de seguida crio uma estrutura de decisão que diz que se o numero de chances for <= 0 envia uma mensagem ao usuario a informar que este perdeu, caso a letra esteja
secreto = 'perfume'
digitadas = []
chances = 3

while True:
    if chances <= 0:
        print('Perdeu!!')
        break

    letra = input('Digite uma letra: ')

    if letra not in secreto:
        chances -= 1
    print(f'Ainda tem {chances} chances!')
    if len(letra) > 1:
        print('Digite apenas uma letra')
        continue

    digitadas.append(letra)
    #print(digitadas)

    # Verificar se a letra secreta encontra-se na palavra secreta
    if letra in secreto:
        print(f'Boa, a letra "{letra}" existe na palavra secreta')
    else:
        print(f'A letra "{letra}" não existe na palavra secreta')
        digitadas.pop()

    # Visualizador
    secreto_temporario = ''
    for letra_secreta in secreto:
        if letra_secreta in digitadas:
            secreto_temporario += letra_secreta
        else:
            secreto_temporario += '*'
    if secreto_temporario == secreto:
        print(f'Ganhouu a palavra secreta é "{secreto}"')
        break
    else:
        print(f'A palavra secreta está assim: {secreto_temporario}')

    print()
