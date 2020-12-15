print('''Среднее из полученных чисел

Программа подсчитывает среднее из введенных чисел''')

print('Введите три числа: ')
a = int(input())
b = int(input())
c = int(input())

if b <a <c or c <a <b:
    print('Среднее:', a)
elif a <b <c or c<b <a:
    print('Среднее:', b)
else:
    print('Среднее:', c)
