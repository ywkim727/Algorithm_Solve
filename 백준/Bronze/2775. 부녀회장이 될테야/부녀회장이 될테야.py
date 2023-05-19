T = int(input())

for _ in range(T) :
    K = int(input())
    N = int(input())
    dp = [i for i in range(1, N+1)]

    for _ in range(K) :
        for i in range(1, N) :
            dp[i] += dp[i-1]
    print(dp[-1])