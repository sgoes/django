"""
while / else
contadores
acumuladores
"""

# the cicle while beggins always with an accountant variable
# contador = 0
# while contador <= 100:
#     print(contador)
#     contador += 1

contador = 1
acumulador = 1

while contador <= 10:
    print(contador, acumulador)

    if contador > 5: #se quiser chegar à contagem acumulada até 5  quiser após isso sair
        break

    acumulador = acumulador + contador
    contador += 1
else:
    print('Cheguei no else!')

