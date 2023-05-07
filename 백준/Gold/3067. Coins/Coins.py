# https://d-cron.tistory.com/23
T = int(input())

coins = []

for _ in range(T) :
    N = int(input())
    coins = list(map(int,input().split()))
    M = int(input())
    
    dp = [0] * (M+1)
    dp[0] = 1

    for coin in coins :
        for i in range(1, M+1) :
            if i >= coin :
                dp[i] += dp[i-coin]
    print(dp[M])