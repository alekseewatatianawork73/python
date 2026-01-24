n, m = map(int, input().split())

a = [list(map(int, input().split())) for i in range(n)]

mx = - 10000
k1, k2 = 0, 0
for i in range(n - 2):
    for j in range(m - 2):
        s = a[i][j] + a[i][j + 1] + a[i][j + 2] + a[i + 1][j] + a[i + 1][j + 1] + a[i + 1][j + 2] + a[i + 2][j] + a[i + 2][j + 1] + a[i + 2][j + 2]
        if s > mx:
            mx = s
            k1, k2 = i + 1, j + 1
print(k1, k2)
