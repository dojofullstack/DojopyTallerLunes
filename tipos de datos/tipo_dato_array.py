# tipo de dato array
#case sentive
""" propiedades type data array
    'append',
    'clear',
    'copy',
    'count',
    'extend',
    'index',
    'insert',
    'pop',
    'remove',
    'reverse',
    'sort'
"""

lista_participantes = []
print(lista_participantes)
print(type(lista_participantes))

lista_participantes = ['carlos', 'luis', 'henry', '123', '23']
lista_participantes_new = lista_participantes.copy()

print(lista_participantes[0])
print(lista_participantes[-1])
print(lista_participantes)

print(len(lista_participantes))
# print(dir(lista_participantes))

lista_participantes.append('david')
# lista_participantes.clear()
lista_participantes_nueva = lista_participantes.copy()
lista_participantes_nueva.append('erick')

lista_participantes.append("sonia")

# print(lista_participantes.count('Henry'))

lista_participantes.extend(['pepe', 'juan'])
# print(lista_participantes)

# print(lista_participantes.index('luis'))
lista_participantes.insert(1, 'maria')
# print(lista_participantes)
lista_participantes.pop(0)
# print(lista_participantes)

lista_participantes.remove('henry')
lista_participantes.remove('maria')
lista_participantes.reverse()
print(lista_participantes)
lista_participantes.sort()
print(lista_participantes)


print(type(list('hola coders')))
