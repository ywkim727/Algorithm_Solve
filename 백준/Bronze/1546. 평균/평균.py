N = int(input())
num = list(map(int, input().split()))

max_num = max(num)
res = []
for i in num :
    res.append(i/max_num*100)
sum = 0
for i in res :
    sum += i

print(sum/len(res))