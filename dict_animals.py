# хранение статей о животных

# 1 способ: в двух списках на соответствующих позициях, в первом - названия животных, во втором - статьи про них
animals = ['fox', 'hare', 'wolf', 'bear']
articles = ['Foxes are small-to-medium-sized omnivorous mammals belonging to several genera...',
            'Hares and jackrabbits are mammals belonging to the genus Lepus...',
            'The wolf, also known as the grey wolf or gray wolf, is a canine native to Eurasia and North America...',
            'Bears are carnivoran mammals of the family Ursidae. They are classified as...']
# найдём и выведем статью о волке
n = len(animals)  # количество статей
for i in range(n):
    if animals[i] == 'wolf':
        print(animals[i], articles[i], sep=' - ')
# => wolf - The wolf, also known as the grey wolf or gray wolf, is a canine native to Eurasia and North America...

# 2 способ: список кортежей, каждый кортеж содержит два элемента - название животного и статью о нём
animals = [('fox', 'Foxes are small-to-medium-sized omnivorous mammals belonging to several genera...'), ('hare', 'Hares and jackrabbits are mammals belonging to the genus Lepus...'), 
           ('wolf', 'The wolf, also known as the grey wolf or gray wolf, is a canine native to Eurasia and North America...'), ('bear', 'Bears are carnivoran mammals of the family Ursidae. They are classified as...')]
# найдём статью о медведе и выведем её
for kortezh in animals:
    animal, article = kortezh  # в каждом кортеже 2 элемента: название животного и статья
    if animal == 'bear':
        print(article)
# =>  Bears are carnivoran mammals of the family Ursidae. They are classified as...

# 3 способ - самый удобный: словарь, в котором значениями являются статьи о животных, а ключом для каждой статьи - название животного
animals = {'fox': 'Foxes are small-to-medium-sized omnivorous mammals belonging to several genera...',
           'hare': 'Hares and jackrabbits are mammals belonging to the genus Lepus...',
           'wolf': 'The wolf, also known as the grey wolf or gray wolf, is a canine native to Eurasia and North America...'}
# найдём и выведем статью о лисе
print(animals['fox'])
# => Foxes are small-to-medium-sized omnivorous mammals belonging to several genera...

# изменение значения в словаре: заменим статью о зайце (hare) на новую
animals['hare'] = 'New article about hare...'
print(animals['hare'])  # => New article about hare...

# добавление нового элемента в словарь: добавим статью о медведе
animals['bear'] = 'Bears are carnivoran mammals of the family Ursidae. They are classified as...'

# удаление элементов из словаря при помощи del
del animals['hare']
print(animals['hare'])  # => ошибка: KeyError: 'hare' - такого ключа больше нет в словаре

# удаление элементов из словаря при помощи pop
d = animals.pop('hare')
print(d)  # => New article about hare...
print(animals['hare'])  # => ошибка: KeyError: 'hare' - такого ключа больше нет в словаре

# что будет, если попробовать удалить несуществующий элемент
d = animals.pop('cat')
print(d)  # => KeyError: 'cat' - такого ключа нет в словаре

# чтобы ошибка не выводилась, можно добавить в pop() второй аргумент - он будет выводиться, если ключа нет в словаре
d = animals.pop('cat', 'Такой статьи нет в словаре')
print(d)  # => Такой статьи нет в словаре

# проверка наличия или отсутствия элемента в словаре
if 'fox' in animals:
    print('У нас есть статья про лису.')
if 'tiger' not in animals:
    print('У нас нет статьи о тигре.')

# поиск статьи при помощи метода get(): ищем статью про волка
my_art = animals.get('wolf')
print(my_art)  # => The wolf, also known as the grey wolf or gray wolf, is a canine native to Eurasia and North America...

# поиск несуществующей статьи
not_art = animals.get('cat')
print(not_art)  # => None - пустое значение

# можем заменить None, добавив второй аргумент в get()
not_art = animals.get('cat', 'Несуществующая статья')
print(not_art)  # => Несуществующая статья

# вывод всех ключей и значений словаря при помощи перебора
for animal in animals:
    print(animal, animals[animal], sep=' - ')
 ''' => 
fox - Foxes are small-to-medium-sized omnivorous mammals belonging to several genera...
hare - New article about hare...
wolf - The wolf, also known as the grey wolf or gray wolf, is a canine native to Eurasia and North America...
bear - Bears are carnivoran mammals of the family Ursidae. They are classified as...
'''

# метод keys() возвращает все ключи словаря, values() - все значения
names = list(animals.keys())  # список ключей - названий животных
articles = list(animals.values())  # список значений - статей о животных

# метод items() - возвращает пары ключ/значение, можно использовать для вывода
for animal, article in animals.items():
    print(animal, article, sep=' - ')


# считывание словарей: Дано n строк с фамилиями и именами людей. Требуется по конкретной фамилии определить имя ученика.

n = int(input())  # количество людей (длина словаря)
people = {}  # пустой словарь для хранения фамилий и имен
# проходимся по каждой из n строк
for i in range(n):
    surname, name = input().split()  # считываем фамилию и имя в переменные surname и name
    people[surname] = name  # добавляем в словарь новый ключ surname со значением name

my_surname = input()  # считываем с экрана какую-то фамилию
print(people[my_surname])  # получаем значение-имя из словаря people по ключу my_surname
