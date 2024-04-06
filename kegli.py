n, m = map(int, input().split())
keg = [0] * n    # список несбитых кеглей

for i in range(m):
    l, r = map(int, input().split())
    for j in range(l, r + 1):
        keg[j] = 1 # сбитые кегли обозначаем 1

s = sum(keg)

print(s)
