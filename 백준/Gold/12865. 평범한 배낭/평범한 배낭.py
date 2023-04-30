N, K = map(int, input().split())

item = [list(map(int, input().split())) for _ in range(N)]

knapsack = [[0] * (K + 1) for _ in range(N)]

for i in range(N) :
    for j in range(1, K+1) :
        w = item[i][0]
        v = item[i][1]

        if j < w :
            knapsack[i][j] = knapsack[i-1][j]
        else :
            knapsack[i][j] = max(knapsack[i-1][j], v + knapsack[i-1][j-w])

print(knapsack[-1][-1])