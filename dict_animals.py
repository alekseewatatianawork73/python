# хранение статей о животных

# 1 способ: в двух списках на соответствующих позициях, в первом - названия животных, во втором - статьи про них
animals = ['fox', 'hare', 'wolf', 'bear']
articles = ['Foxes are small-to-medium-sized omnivorous mammals belonging to several genera...',
            'Hares and jackrabbits are mammals belonging to the genus Lepus...',
            'The wolf, also known as the grey wolf or gray wolf, is a canine native to Eurasia and North America...',
            'Bears are carnivoran mammals of the family Ursidae. They are classified as...']
# выведем статью о волке
print(animals[2], articles[2], sep=' - ')  # => wolf - The wolf, also known as the grey wolf or gray wolf, is a canine native to Eurasia and North America...

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
           'wolf': 'The wolf, also known as the grey wolf or gray wolf, is a canine native to Eurasia and North America...', 
           'bear': 'Bears are carnivoran mammals of the family Ursidae. They are classified as...'}
