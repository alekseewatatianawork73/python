#циклический сдвиг элементов вправо
a = list(map(int, input().split()))
temp = a[-1]
for i in range(len(a)-1, 0, -1):
    a[i] = a[i-1]
a[0] = temp
print(*a)

#циклический сдвиг элементов влево
a = list(map(int, input().split()))
temp = a[0]
for i in range(0, len(a)-1):
    a[i] = a[i+1]
a[-1] = temp
print(*a)
