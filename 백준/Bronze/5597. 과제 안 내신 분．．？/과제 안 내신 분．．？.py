num = []
for _ in range(28) :
    num.append(int(input()))

num.sort()
res = []


for i in range(1, 31) :
    if i in num :
        continue
    else :
        res.append(i)

for i in res :
    print(i)

