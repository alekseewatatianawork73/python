# наиболее частый элемент (H)
n = int(input())
a = list(map(int, input().split()))
b = [0]*101
for x in a:
    b[x] += 1
m = max(b)
for i in range(len(b)-1, -1, -1):
    if b[i] == m:
        print(i)
        break

n = int(input())
a = list(map(int,input().split()))
a.sort()
mx = 0
imx = 0
for x in a:
    if a.count(x)>=mx:
        mx = a.count(x)
        imx = x
print(imx)
