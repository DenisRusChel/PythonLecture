#  3. Напишите программу, в которой пользователь будет задавать две строки, а программа -
# # определять количество вхождений одной строки в другой.

# text1 = "aaa"
# text2 = 'aaabbbaaa'
# print(text2.count(text1)

# unique_in_order('AAAABBBCCDAABBB') == ['A', 'B', 'C', 'D', 'A', 'B']
# unique_in_order('ABBCcAD')         == ['A', 'B', 'C', 'c', 'A', 'D']
# unique_in_order([1,2,2,3,3])       == [1,2,3]

# b = 'AAAABBBCCDAABBB'
# a= list(b)
# c=set(b)

# print(c)

text2 = 'aaabbbaaa'
cach = ''
l = []
for el in text2:
    if el != cach:
        l.append(el)
        cach = el
print(l)