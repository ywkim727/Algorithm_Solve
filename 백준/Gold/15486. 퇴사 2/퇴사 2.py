import sys
N = int(sys.stdin.readline())

t = [0 for _ in range(N+1)]
p = [0 for _ in range(N+1)]
dp = [0 for _ in range(N+1)]

for i in range(N) :
    a,b = map(int, sys.stdin.readline().split())
    t[i] = a
    p[i] = b

for i in range(len(t)-2, -1, -1) :              #역순으로 진행, 마지막날 상담은 어차피 못하기 때문에 볼 필요 없음
    if t[i]+i <= N :                            #날짜를 초과하지 않아 상담을 할 수 있을경우
        dp[i] = max(dp[i+1], p[i]+dp[t[i]+i])   #상담을 하거나, 안하거나 최대 수익을 선택
    else :                                      #날짜를 초과해 상담을 못할경우
        dp[i] = dp[i+1]

print(dp[0])