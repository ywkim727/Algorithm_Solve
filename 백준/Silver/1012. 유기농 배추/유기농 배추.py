import sys
from collections import deque 

def bfs(graph, a, b) :
    graph[a][b] = 0
    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]
    q = deque()
    q.append((a,b))
    while q :
        x, y = q.popleft()
        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= M :
                continue
            if graph[nx][ny] == 1 :
                graph[nx][ny] = 0
                q.append((nx,ny))

T = int(sys.stdin.readline())

for _ in range(T) :
    N, M, K = map(int, sys.stdin.readline().split())
    bachu = [[0]*(M) for _ in range(N)]
    bug = 0
    for _ in range(K) :
        X, Y = map(int, sys.stdin.readline().split())
        bachu[X][Y] = 1
    for i in range(N) :
        for j in range(M) :
            if bachu[i][j] == 1 :
                bug += 1
                bfs(bachu,i,j)
    print(bug)