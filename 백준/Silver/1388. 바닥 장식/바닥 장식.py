import sys
sys.setrecursionlimit(10**7)
def dfs(x, y) :
    if graph[x][y] == '-' :
        graph[x][y] = 1                                 #1을 넣어주어 방문처리
        for _y in [-1, 1] :                             # - 만나면 좌우를 탐색
            ny = y + _y                                 # | 만나면 상하를 탐색
            if (0 < ny < M) and graph[x][ny] == '-' :
                dfs(x,ny)
    if graph[x][y] == '|' :
        graph[x][y] = 1
        for _x in [-1, 1] :
            nx = x + _x
            if (0 < nx < N)  and graph[nx][y] == '|' :
                dfs(nx, y)
    

N, M = map(int, input().split())
graph = []

for _ in range(N) :
    graph.append(list(input().rstrip()))

count = 0
for i in range(N) :
    for j in range(M) :
        if graph[i][j] == '-' or graph[i][j] == '|' :   #반목문으로 dfs호출, 다른 바닥 만나거나 범위를 벗어나면 함수 종료되면서 count++
            dfs(i,j)
            count += 1
print(count)