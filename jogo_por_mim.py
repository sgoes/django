secreto = 'maravilha'
digitada = []
chances = 3

while True:

    letra = input("Digite uma letra: ")
    if len(letra) > 1:
        print('Insira apenas uma letra')

        continue
        digitada.append(letra)

    if letra not in secreto:
        chances -= 1

    if letra in secreto:
        print('Acertaste numa letra!')
    else:
        print('Não acertaste')

    secreto_temporario = ''
    for letra_secreta in secreto:
        if letra_secreta in digitada:
            secreto_temporario += letra_secreta
        elif secreto_temporario == secreto:
            print("Voce ganhou")
        else:
            secreto_temporario += '*'




