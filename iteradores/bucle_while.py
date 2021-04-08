import time

# python bucle while
soy_freelancer = True
contador = 0
contador_desc = 10
mis_numeros = list(range(100))
# print(mis_numeros)

while soy_freelancer:
    while contador_desc:
        contador_desc -= 1
        print(contador_desc)

    for value in mis_numeros:
        if value == 50:
            print(f'value del for: {value}')
    time.sleep(0.2)
    contador += 1
    if contador == 5:
        soy_freelancer = False
        # break
    print('soy freelancer')


print('sali del while!')
