piece = list(map(int, input().split()))
res = [1, 1, 2, 2, 2, 8]
ans = []
for i in range(len(piece)) :
    ans.append(res[i]- piece[i])

for i in ans :
    print(i, end=" ") 