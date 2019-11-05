import random
import os

print('''
Монетка 2.0 | usu4lc0d3r (c)
Вводи варианты, между которыми выбрать, один за другим
Введи 0, чтобы сделать выбор''')

choises = []
while True:
    b = input('\nВвод: ')
    if b == '0':
        break
    else: 
        choises.append(b)

if len(choises) == 0:
    print('Ничего не введено. Всего доброго! :D')
    exit()
else: 
    choise = random.randint(0, len(choises) - 1)
    try:
        print('Мой выбор: ', choises[choise])
    except IndexError:
        print('Выбрать из одного пункта невозможно. Совсем. Никак. Ибо выбор только один.')
