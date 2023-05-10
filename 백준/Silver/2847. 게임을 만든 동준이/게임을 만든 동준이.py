N = int(input())
num = []
count = 0
for _ in range(N) :
    num.append(int(input()))

for i in range(N-1, 0, -1) :
    while num[i] <= num[i-1] :
        num[i-1] -= 1
        count += 1

print(count)