import time

print('Calculator v 1.0')

time.sleep(2)
print()
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
print('Для завершения работы программы введите ноль')
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
print()
time.sleep(2)
while True:
        print()
        choice = input('''Пожалуйста выберите какую операцию вы хотите провести : 
+ для сложения
- для вычитания
* для умножения
/ для деления
... : 
''')
        if choice == '0': break
        if choice in ('+','-','*','/'):
                x = int(input('Введите первое число: '))
                y = int(input('Введите второе число: '))
                if choice == '+':
                        print('Ответ: ' , x + y)
                elif choice == '-':
                        print('Ответ: ' , x - y)
                elif choice == '*':
                        print('Ответ: ' , x * y)
                elif choice == '/':
                        if y != 0:
                                print('Ответ: ' , x / y)
                        else:
                                print('На ноль делить нельзя, родной!')
        else:
                print('Неверный знак операции!')


        time.sleep(5)