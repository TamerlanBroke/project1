def lab4n1():
    try:
        a = int(input('Чтобы проверить деление на 3 ,введите число : '))
        b = a % 3
    except ValueError:
        print('Введите число !')
    except ZeroDivisionError:
        print("Число ноль")
    else:
        if int(a) % 3 == 0:
            print('Число', a , 'делятся на 3!')
        else:
            print('Число', a , 'не делятся на 3!')


def lab4n2():
    try:
        a = int(input('Введите число - '))
        b = 100 / a
    except ZeroDivisionError:
        print('Введен ноль')
    except ValueError:
        print('Введено не число')
    else :
        print('Результат деление 100 на введенное число:' , b )


def lab4n3():
    data = input('Введите дату в формате дд.мм.гггг: ')
    data = data.split('.')
    if int(data[0])*int(data[1]) == int(data[2][2:4]):
        print('Ваша  дата рождения  магическая! :)')
    else:
        print('К сожелению у вас обычная дата рождение :( ')


def lab4n4():
    a = input("Введите 6 цифр")
    for i in range(len(a)):
        if int(a[0]) + int(a[1]) + int(a[2]) == int(a[3]) + int(a[4]) + int(a[5]):
            print("Счастливый билет")
            break
        else:
            print("Не счастливый")
            break




lab4n1()
lab4n2()
lab4n3()
lab4n4()