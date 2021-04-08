
# tipo de dato dict

usernames = {
    'user1': 'henry',
    'user2': 'henry',
    'age': 25,
    'email': 'hola@dojopy.com',
    1: ['a', 'b'],
    True: ['c'],
    'otrodict': {
        'mykey': 'myvalue'
    }
}

print(usernames)
print(type(usernames))
print(dir(usernames))
print(len(usernames))
print(usernames['email'])

# print(usernames.clear())
print(usernames.keys())
print(usernames.values())

usernames['email'] = 'henry@dojopy.com'
usernames['lastname'] = 'cristofer'
# print(usernames)

# print(usernames['email2'])
# print(usernames.get('email2', ''))
# print(usernames.pop('user1'))
# print(usernames)
# print(usernames.popitem())
# print(usernames)

usernames.update({'direccion': 'lima', 'countryArea': '51'})

usernames_new = usernames.copy()
usernames_new['phone'] = '5193548952'
print(usernames_new)
print(usernames)

nueva_dict = dict([['nombre', 'paul'], ['apellido', 'sanchez']])
print(type(nueva_dict))
