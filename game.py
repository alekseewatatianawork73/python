from random import *

d = randint(1, 100)

print('Угадайте число:')
a = int(input())
count = 10
ans = 'да'
while ans == 'да':
    while count > 0:
        if a > d:
            print('Введите число поменьше.')
        elif a < d:
            print('Введите число побольше.')
        else:
            print('Вы угадали число!')
            break
        print('Угадайте число:')
        a = int(input())
        count -= 1
    
    if count > 7:
        print('Вы везунчик! :)')
    elif count > 4:
        print('Вы неплохо справились.')
    elif count > 1:
        print('Unluck! Вы алкаш!')
    else:
        print('У вас закончились попытки :(')

    while True:
        ans = input('Хотите ли вы продолжить игру? (да/нет)')
        if ans != 'да' and ans != 'нет':
            print('Вы ввели некорректный ответ!')
            continue
        if ans == 'нет':
            break
        d = randint(1, 100)
        print('Угадайте число:')
        a = int(input())
        count = 10
        break
            
print('Игра завершена. Идите пить => toilet')
