# ввод, вывод и арифметика
a, b, c = 1, 2, 3
print(a, b, c, sep='*')
print(a, end='-')
print(b)

# f-строки
age = int(input())
name = input()
rate = float(input())

print(f'Меня зовут {name}. Мне {age} лет.')

# задача про количество людей в автобусах
x = int(input())
n = int(input())
p = x // n
o = x % n

# условия (переводим проценты в оценку)
''' if-elif-else'''
n = int(input())
if n > 85:
    print(5)
elif n > 65:
    print(4)
elif n > 45:
    print(3)
else:
    print(2)



# while (делим число на 2 до тех пор, пока оно не станет нечётным)
n = int(input())
k = 0
while n % 2 == 0:
    n = n // 2
    k += 1
print(n)

# ищем максимум среди четных чисел
n = int(input())
mx = -1000000000000000
while n != 0:
    if n > mx and n % 2 == 0:
        mx = n
    n = int(input())

# количество чисел, кратных 3
n = int(input())
k = 0
while n != 0:
    if n % 3 == 0:
        k += 1
    n = int(input())

# сумма положительных чисел
n = int(input())
k = 0
while n != 0:
    if n > 0:
        k = k + n
    n = int(input())


# количество чисел, оканчивающихся на 2
n = int(input())
k = 0
while n != 0:
    if n % 10 != 2:
        k += 1

#for
for i in range(start = 0, stop, step = 1)
range(5)
# => 0 1 2 3 4
range(2, 7)
# => 2 3 4 5 6
range(3, 100, 3)
# => 3 6 9 ... 96 99
range(102, 1, -2)
# => 102 100 98 ... 4 2


s = 'чебурашка'
for x in s:
    print(x, end='*')
'''
ч*е*б*у*р*а*ш*к*а*
'''


# количество положительных чисел
n = int(input())
k = 0
for i in range(n):
    x = int(input())
    if x > 0:
        k += 1
print(k)
'''
5
7
9
3
-1
0
'''
# простые числа
n = int(input())
s = 'yes'
for i in range(2, n):
    if n % i == 0:
        s = 'no'
        break
print(s)
        


