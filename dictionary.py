##Группа детей хочет посетить один из аттракционов в парке, но на этот аттракцион пускают не всех. Есть ограничение: его могут посещать лишь те, кто достиг 160 см в росте. Требуется определить, кто сможет пойти на аттракцион.
##Пользователь вводит целое число N - количество детей, желающих посетить аттракцион. Далее следуют N строк, содержащих информацию о росте каждого ребёнка. Выведите имена тех детей, которые могут посетить аттракцион.
n = int(input("Количество детей: "))
children = dict()
for i in range(n):
    a, b, c = input().split()
    name = a + " " + b
    height = int(c)
    children[name] = height
print("\nИмена допущенных на аттракцион:")
for k in children:
    if children[k] >= 160:
        print(k)
