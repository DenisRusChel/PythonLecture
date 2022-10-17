# 1. Реализуйте алгоритм задания случайных чисел без использования встроенного 
# генератора псевдослучайных чисел.



import datetime


n = datetime.datetime.now().microsecond%10

print(n*(max-min))

# def random_number(minimum,maximum):
#     now = str(time.ctime())
#     rnd = float(now[::-1][:3:])/1000
#     return minimum + rnd*(maximum-minimum)

# print(random_number(1,100))
 

