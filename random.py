from random import *
ar = ["a", "b", "c", "d", "e"]
s = "1234567890"
a = random()                  # случ. вещественное число от 0 до 1

b = randint(1, 100)           # случ. целое число в интервале [1, 100] 

c = randrange(1, 100, 2)      # случ. целое нечётное число от 1 до 100 невключительно

d = uniform(1, 2)             # случ. вещественное число от 1 до 2

e = choice(ar)                # случ. элемент из списка ar

f = sample(s, 5)              # список из 5 случайных символов строки s

shuffle(ar)                   # перемешивает список ar (к строкам применять нельзя)

print(a)
print(b)
print(c)
print(d)
print(e)
print(*ar)
print(f)
