#     1. Напишите программу, которая принимает на вход число N и выдаёт последовательность из N членов.
#         *Пример:*
#         - Для N = 5: 1, -3, 9, -27, 81


from asyncio.windows_events import NULL

N = int(input('Введите число N: '))
j=1

for i in range(N):
    print(j)
    j = j*-3


