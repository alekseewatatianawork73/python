from math import *
n, k, m, x = map(int, input().split())

# 1 вариант
s1 = n * k
# 2 вариант
k = ceil(n / m) # floor
s2 = x * k

if s1 < s2:
    print(1)
elif s2 < s1:
    print(2)
else:
    print(3)
