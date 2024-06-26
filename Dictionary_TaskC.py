n = int(input())  # количество строк
d = {}  # словарь для хранения документов каждого студента (имя - ключ, множество документов - значение)
all_docs = set()  # множество для хранения всех необходимых документов; выбрали множество, т. к. в нём элементы не повторяются

for i in range(n):
    doc, name = input().split()

    # если имени студента ещё нет нет в словаре, создаём для него пустое множество для хранения его документов
    if name not in d:
        d[name] = set()

    d[name].add(doc)  # добавляем документ во множество студента
    all_docs.add(doc) # добавляем документ в общее множество всех документов

# считаем количество документов, которых не хватает у каждого студента
count = 0
for x in d.values():
    # от общего количества необходимых документов отнимаем количество документов конкретного студента
    count += len(all_docs) - len(x)
print(count)
