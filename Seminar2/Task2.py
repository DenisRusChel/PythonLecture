# 2. Для натурального n создать словарь индекс-значение, состоящий из элементов последовательности 3n + 1.
# #         *Пример:*
# #         - Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}

n = int(input('Введите число n: '))
dict_n = {b:b*3+1 for b in range(1,n+1)}
print(dict_n)