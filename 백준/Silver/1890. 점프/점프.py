N = int(input())

graph = [list(map(int, input().split())) for _ in range(N)]

dp = [[0] * (N) for _ in range(N)]          # dp : 각 칸으로 갈 수 있는 경우의 수
dp[0][0] = 1
for i in range(N) :
    for j in range(N) :
        jump = graph[i][j]                  # jump : 점프할 수 있는 거리
        if jump == 0 :                      # 점프가 0이면 더 이상 진행을 막는 종착점
            continue
        if (i + jump) < N :                 # 아래로 점프 했을때 (점프한 거리가 범위를 벗어나지 않는다면)
            dp[i+jump][j] += dp[i][j]              # 점프로 도착한 칸에 + 1
        if (j + jump) < N :                 # 오른쪽으로 점프 했을때
            dp[i][j+jump] += dp[i][j]              # 도착한 칸에 + 1
            
print(dp[-1][-1])                           # dp 출력값 [[0, 0, 1, 0], [0, 1, 0, 3], [2, 1, 1, 1], [1, 2, 2, 3]]