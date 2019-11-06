from random import choice as ch

print('''\nМонетка 2.0 | usu4lc0d3r (c)
Вводи варианты, между которыми выбрать, один за другим
Введи 0, чтобы сделать выбор''')

choices = []
while True:
    b = input('\nВвод: ')
    if b == '0':
        break
    else: 
        choices.append(b)

if len(choices) == 0:
    print('Ничего не введено. Всего доброго! :D')
    exit()
else: 
    choice = ch(choices)
    try:
        print('Мой выбор: ', choice)
    except IndexError:
        print('Выбрать из одного пункта невозможно. Совсем. Никак. Ибо выбор только один.')
