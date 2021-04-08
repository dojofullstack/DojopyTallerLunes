# Python bucle For
# mis_proyectos = 'hola'
# mis_proyectos = ('dojopy', 'storewai')
# mis_proyectos = {'dojopy': '4 años', 'storewai': '1 año'}
# mis_proyectos = {'dojopy', 'storewai'}
mis_proyectos = ['dojopy', 'storewai', 'fullstack.dojopy']
mi_equipo = ['camila', 'jhon', 'henry']
nuevos_proyectps = []

for i, value in enumerate(mis_proyectos):
    for item2 in mi_equipo:
        print(item2)
        # print(f'\t {item2} \n')
    print(i)
    # if i == 1:
    #     break

    # if len(value) == 8:
    #     continue

    # if 'fullstack' in value:
    #     print('rompiendo bucle')
    #     break

    if value == 'dojopy':
        print('genial proyecto!')
    else:
        print(value)

    nuevos_proyectps.append(f'{value} {i} nuevo')

print(nuevos_proyectps)

print('#####'*10)

lista_de_coders = ['henry', 'dave', 'carlos', 'luis', 'miguel']

# nuevos_proyectos_new = [
#     f'{value} {i} nuevo'
#     for i, value in enumerate(lista_de_coders)
#     if len(value) >= 5
#     ]

# print(nuevos_proyectos_new)
