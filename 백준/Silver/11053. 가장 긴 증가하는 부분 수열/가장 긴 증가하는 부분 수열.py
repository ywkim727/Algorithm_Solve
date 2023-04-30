N = int(input())
num = list(map(int, input().split()))

dp = [1 for _ in range(N)]

#자기보다 작은 숫자중 가장 큰 길이를 구하고 +1

for i in range(N) :
    for j in range(i) :
        if num[i] > num[j] :
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))