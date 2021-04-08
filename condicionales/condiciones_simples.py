
# condiciones simples
game_preferido = 'mario bros x'
game_dificultad = '3'

if 'mario' in game_preferido and game_preferido == 'mario bros x':
    print('si es mi juego preferido')
    if game_dificultad == '3':
        print('si es de nivel 3')
        if len(game_dificultad) == 1:
            print('ok')
else:
    print('no juego mario bros ;p')


print('#############################')
print('condicional anidada')

serie_favorita = input('¿cual es serie preferida?')

if serie_favorita == 'años maravillos':
    print('genial!')
elif serie_favorita == 'gambito de damas':
    print('super heroies!')
elif 'gambito' in serie_favorita:
    print('el ajedrez de encanta!')
else:
    print('no te gustan las series :p')


print('##########')
# print(dir(serie_favorita))

if serie_favorita.find('gambito') >= 0 and len(serie_favorita) > 5 and not serie_favorita.isalnum():
    print('es valido!')
else:
    print('no valid ;()')
