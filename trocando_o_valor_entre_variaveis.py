x = 10
y = 'Luis'

z = x
x = y
y = z

print(f'x = {x} e y = {y}')

# no python existe uma forma mais facil de fazer isto
x, y = y,x # x está a receber o valor de y e y está a receber o valor de x
print(f'x = {y} e y = {x}')


