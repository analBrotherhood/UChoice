import random
import os

'''
Специально для Planet Express Team
'''

def cls():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

cls()
print('\nМонетка 2.0 (С) Usu4lC0d3r')
print('\nПоочередно вводи то, между чем выбрать')
print('\nВведи 0, чтобы выбрать')

choises = []
while True:
    b = input('\nВвод: ')
    if b == '0':
        break
    else: 
        choises.append(b)

if len(choises) == 0:
    print('Ничего не введено. Пока!')
    exit()
else: 
    choise = random.randint(1, len(choises))
    try:
        print('Итааак, я выбираю: ', choises[choise])
    except IndexError:
        print('Выбрать из одного пункта невозможно. Совсем. Никак. Ибо выбор только один.')
