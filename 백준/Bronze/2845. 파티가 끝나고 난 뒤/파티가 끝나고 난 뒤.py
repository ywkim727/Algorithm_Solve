L, P = map(int, input().split())
people = list(map(int, input().split()))
res = []
for i in people :
    j = i - L*P
    res.append(j)

for i in res :
    print(i, end=' ')