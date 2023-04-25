#7576번 문제의 3차원 버전 
from collections import deque
M, N, H = map(int, input().split())
tomato = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]
def bfs() :
    dx = [0, 0, -1, 1, 0, 0]
    dy = [1, -1, 0, 0, 0, 0]
    dz = [0, 0, 0, 0, 1, -1] 
    q = deque()
    for i in range(H) :
        for j in range(N) :
            for k in range(M) :
                if tomato[i][j][k] == 1 :
                    q.append([i,j,k])
    while q :
        z, x, y = q.popleft()                               # (주의)z,x,y 순으로 접근해야 한다
        for i in range(6) :
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]
            if nx >= N or nx < 0 or ny >= M or ny < 0 or nz >= H or nz < 0 :
                continue
            else :
                if tomato[nz][nx][ny] == 0 :
                    tomato[nz][nx][ny] = tomato[z][x][y] + 1
                    q.append([nz,nx,ny])
result = 0
bfs()
for i in tomato :
    for j in i :
        for k in j :
            if k == 0 :
                print(-1)
                exit(0)
        result = max(result, max(j))

print(result-1)