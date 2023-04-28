# import sys
# sys.setrecursionlimit(10**7)
#Top-Down
n = int(input())
memoization = [0] * (n+1)

def fibonacci(n) :
    if n == 1 or n == 2 :
        return 1
    if memoization[n] != 0 :
        return memoization[n]
    memoization[n] = fibonacci(n-1) + fibonacci(n-2)
    return memoization[n]

print(fibonacci(n))

#Bottom-Up
# n = int(input())
# dp = [0] * (n+1)

# dp[1] = 1
# dp[2] = 1

# for i in range(3, n+1) :
#     dp[i] = dp[i-1] + dp[i-2]

# print(dp[n])