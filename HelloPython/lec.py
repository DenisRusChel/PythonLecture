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


# import numbers


# text = 'съешь немного чего хочется'
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



# def f(x):
#     if x == 1:
#         return 'Целое'
#     elif x == 2.3:
#         return 23
#     else:
#         return

# arg = 1
# print(f(arg))

# --------------------------------- Работа с файлами --------------------------------

# colors = ['red', 'green', 'blue356']
# data = open('file.txt', 'a')
# data.writelines(colors)
# data.write('\nline\n')
# data.write('\nline2\n')
# data.close()

# with open('file.txt', 'a') as data:
#     data.write('line56\n')
#     data.write('line5633\n')

# path = "file.txt"
# data = open(path, 'r')
# for i in data:
#     print(i)
# data.close()


# --------------------------------- Функции и модули --------------------------------

# import hello as h
# print(h.f(1))

# def new_string(symbol, count=8):
#     return symbol * count
# print(new_string('!', 5))
# print(new_string('!'))
# print(new_string('z'))

# from operator import itemgetter


# def concatenatio(*params):
#     res: str = ""
#     for i in params:
#         res += i
#     return res

# print(concatenatio('a', 'b', 'z'))
# print(concatenatio('a', '1', '3'))


# --------------------------------- Рекурсия --------------------------------

# def fib(n):
#     if n in [1, 2]:
#         return 1
#     else:
#         return fib(n-1) + fib(n-2)
    
# list = []
# for e in range(1,10):
#     list.append(fib(e))
# print(list)

# --------------------------------- Кортежи  --------------------------------
# - это неизменяемый список

# a = (3, 5, 8, 9)
# print(a)
# print(a[0], a[2], a[-1])

# for i in a:
#     print(i)

# t = ()
# print(type(t))
# t = (1,)
# print(type(t))
# t = (1)
# print(type(t))
# t = (1, 5, 9876, 43536)
# print(type(t))

# colors = ['red', 'green']
# print(colors)
# t = tuple(colors)
# print(t)
# t = colors
# print(t)

# t = ('red', 'green')
# print(t)
# a = list(t)
# print(a)

# t = tuple(['red', 'green', 'blue'])
# print(t[0])
# print(t[-1])

# t = tuple(['red', 'green'])
# red, green = t
# print('r:{} g: {}'.format(red, green))


# --------------------------------- Словари  --------------------------------
# - это неупорядоченные коллекции произвольных объектов с доступом по ключу.


# from select import kevent
# from turtle import down


# dictionary = {}
# dictionary = \
#     {
#         'up': 'вверх',
#         'down': 'вниз'
#     }
# print(dictionary)
# print(dictionary['down'])

# for k in dictionary.keys():
#     print(k)

# for k in dictionary.values():
#     print(k)

# for v in dictionary:
#     print([v])

# del dictionary ['up']
# print(dictionary)


# --------------------------------- Множества  --------------------------------
# - содержит в себе уникальные элемунты

# colors = {'red', 'green', 'blue'}
# print(colors)
# colors.add('black')
# print(colors)
# colors.remove('black')
# print(colors)
# colors.remove('black')
# print(colors)
# colors.clear()
# print(colors)

# a = {1,2,3,5,8}
# b = {2,3,8,13,21}
# c = a.copy()
# print(c)
# u = a.union(b)
# print(u)
# i = a.intersection(b)
# print(i)
# dl = a.difference(b)
# print(dl)

# q = a \
#     .union(b)\
#     .difference(a.intersection(b))
# print(q)

# s = frozenset(a)

# --------------------------------- Более глубокая теория по спискам  --------------------------------

# list1 = [1,2,3,4,5]
# list1.insert(3, 11)
# print(list1)

# list1 = [1,2,3,4,5]
# list1.pop()
# print(list1)


# list1 = [1,2,3,4,5]
# list1.append(25)
# print(list1)

# list1 = [1,2,3,4,5]
# list2 = list1

# for e in list1:
#     print(e)

# print()

# for e in list2:
#     print(e)

# list1[0] = 123
# list2[2] = 568

# for e in list1:
#     print(e)

# print()

# for e in list2:
#     print(e)