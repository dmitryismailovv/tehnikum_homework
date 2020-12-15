import time

name_list = []
age_list = []
phone_number_list = []
clients_list = []


while True:
    print('Доброго времени суток, уважаемый пользователь!')
    time.sleep(1)
    print('''Вас приветствует MAKHMOOD AKA! 
Бот, который поможет Вам вести учёт всех ваших пользователей.''')
    print()
    time.sleep(1)
    print('MAKHMOOD AKA собирает ваши данные для дальнейшего удобства использования CRM системой')
    print('Согласны ли вы на обработку данных?')
    a = input('ДА согласен(на) / НЕТ не согласен(на) :  ')
    if a == 'Да' or a == 'да':
        time.sleep(3)
        print()
        print('Благодарим Вас за доверие!')
        time.sleep(1)
    elif a =='Нет' or a == 'нет':
        time.sleep(3)
        print()
        print('В данном случае я никак не смогу помочь вам с распределением ваших клиентов в CRM систему')
        print()
        time.sleep(1)
        print('''
        Мы живем в век технологий. Обработка личных данных только улучшает Вашу жизнь.
        С Вашего позволения, узнав о Вас больше, некоторые сайты по типу Amazon.com смогут подбирать товары исходя из Ваших предыдущих покупок.
        Apple Music или Yandex Музыка сделают Ваш день краше с новой подборкой музыки каждое утро, также получая данные о Ваших музыкальных вкусах.
        Instagram.com сможет подобрать для Вас ленту фотографий, которые вы скорее всего не оставите без Вашего внимания и царского лайка.
        И это только самая малая часть того, что я могу вам поведать об обработке данных.
        Так и я смогу внести Вас в свою базу данных для нашего дальнейшего сотрудничества, создавая для вас лучшие условия для ведения бизнеса''')
        time.sleep(15)
        print()
        time.sleep(5)
        print()
        print('Я верю в то, что вы сделаете правильный выбор')
        print('Напишите мне ДА и мы продолжим. Ответ НЕТ не принимается')
        choice_2 = input('Ваш ответ: ')




    name = str(input('Введите ваше имя: '))
    age = int(input('Введите ваш возраст: '))
    phone_number = int(input('Введите ваш номер телефона: '))
    print()
    time.sleep(0.7)
    print('Загрузка..')
    print()
    time.sleep(5)
    print('Выдаю результат..')
    print()
    time.sleep(1)
    print('Вас зовут - ', name)
    print('Вам - ', age ,)
    print('Ваш номер телефона - ' , phone_number)
    print()
    time.sleep(1)
    print('Все верно? : ')
    agree = input('Да ' '/' ' Нет ')
    if agree != 'Да':
        print('Что бы вы хотели изменить?')
        change = input('Имя ' '/' ' Возраст ' '/' ' Номер телефона ' ': ')
        if change == 'Имя' or 'имя':
            new_name = input('Введите своё имя повторно: ')
            name = new_name

        elif change == 'Возраст' or change == 'возраст':
            new_age = input('Введите свой возраст повторно: ')
            age = new_age

        elif change == 'Номер телефона' or change == 'номер телефона' or change == 'номер':
            new_phone_number = input('Введите свой номер телефона повторно: ')
            phone_number = new_phone_number

        else:
            print('Попробуйте писать по шаблону.')


    clients_name = name
    clients_age = age
    clients_phone_number = phone_number
    clients_list.append(clients_name)
    clients_list.append(clients_age)
    clients_list.append(clients_phone_number)

    print()
    print()
    print()
    print()
    print()
    print()
    print()

