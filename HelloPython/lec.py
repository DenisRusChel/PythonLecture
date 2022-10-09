# print('Hello world')

# Типы данных и переменная
# int, float, boolean, str, list, None
# value = None

# print(type(a))
# print(type(b))
# print(type(value))
# value = 1234
# print(type(value))

# a = 123
# b = 1.23
# s = "hello world"
# print(a, b, s)
# print(a, 'мир', b, s)
# print('{2} мир {1} {0}'.format(a, b, s))
# print(f'{a} {b} {s}')
# print(f'{b} {a} {b}')

# f = False
# print(f)

# list = [1, 2, 'world', 4, 5.34, True]
# col = [1, 2, 'world', 4, 5.34, True]
# print(list)
# print(col)

# print('Введите а');
# a = float(input())
# print('Введите b');
# b = float(input())
# print(a, '+' ,b, '=', a+b)
# # print('{} {}' .format(a, b))
# # print(f'{a} {b}')


# a = 1.312
# b = 3
# c = round(a * b, 2)
# print(c)

# a = [1,2,3,10]
# # print(a)
# # print(not 5 in a)

# is_odd = not a[2] % 2
# print(is_odd)

# a = int(input('a = '))
# b = int(input('b = '))
# if a>b:
#     print('a > b', '→', a)
# else:
#     print('b > a', '→', b)

# username = input('Введите имя: ')
# if username == 'Маша':
#     print('Ура это же МАША!!!')
# elif username == 'Даша':
#     print('Ура Ура Ура!!!')
# elif username == 'Денис':
#     print('Денис - лучший!!!')
# else:
#         print('Привет username')

# original = 1566
# inverted = 0
# while original != 0:
#     inverted = inverted * 10 + (original % 10)
#     original //=10
#     print(original)
# else:
#     print('Пожалуй')
#     print('Хватит')
# print(inverted)


# for i in 'qwerty-den':
#     print(i)


import numbers


text = 'съешь немного чего хочется'
# print(len(text))
# print('немного' in text)
# print(text.isdigit())
# print(text.islower())
# print(text.replace('немного', 'МНОГО'))


# print(text[5])
# print(text[len(text)-1])
# print(text[-5])
# print(text[:])
# print(text[3:9])
# print(text[len(text)-4:])
# print(text[2:-5])
# print(text[0:len(text):5])


# ran = range(2, 9, 2)
# numbers = list(ran)
# print(numbers)

# numbers[0] = 5
# print(numbers)

# for i in numbers:
#     i*=2
#     print(i)
# print(numbers)
# print(len(numbers))


# colors = ['red', 'green', 'blue', 'white']


# for b in colors:
#     print(b)

# for b in colors:
#     print(b*2)

# colors.append('black')
# print(colors)
# colors.remove('green')
# print(colors)
# del colors[2]
# print(colors)



def f(x):
    if x == 1:
        return 'Целое'
    elif x == 2.3:
        return 23
    else:
        return

arg = 1
print(f(arg))





















