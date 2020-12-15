print('''Среднее из полученных чисел

Программа подсчитывает наибольшее из введенных чисел''')

print('Введите три числа: ')
a = int(input())
b = int(input())
c = int(input())

m = a
if m < b:
    m = b
if m < c:
    m = c
print('Наибольшее число : ')
print(m)
