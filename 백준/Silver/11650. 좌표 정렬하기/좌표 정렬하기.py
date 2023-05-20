N = int(input())

num = []

for _ in range(N) :
    x, y = map(int, input().split())
    num.append((x,y))

num.sort(key = lambda x : (x[0],x[1]))


for i in range(N) :
    print(num[i][0], num[i][1])