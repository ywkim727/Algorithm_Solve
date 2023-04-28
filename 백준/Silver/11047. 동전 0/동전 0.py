N, K = map(int, input().split())

coins = []
count = 0

for _ in range(N) :
    coins.append(int(input()))

coins.sort(reverse=True)

for i in coins :
    count += K // i
    K %= i

print(count)