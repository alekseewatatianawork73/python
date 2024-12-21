a = int(input())
mx = -20000000
while a != 0:
    if a > mx and a % 2 != 0:
        mx = a
    print(mx)
    a = int(input())
