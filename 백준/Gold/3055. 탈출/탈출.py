from collections import deque
def bfs(Dx, Dy) :
    while q :
        x, y = q.popleft()
        if map[Dx][Dy] == 'S' :
            return visited[Dx][Dy]
        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]            
            if nx >= R or nx < 0 or ny >= C or ny < 0 :
                continue
            else :
                if (map[nx][ny] == '.' or map[nx][ny] == 'D') and map[x][y] == 'S' :
                    map[nx][ny] = 'S'
                    visited[nx][ny] = visited[x][y] + 1
                    q.append((nx,ny))
                elif (map[nx][ny] == '.' or map[nx][ny] == 'S') and map[x][y] == '*' :
                    map[nx][ny] = '*'
                    q.append((nx,ny))
    return "KAKTUS"

R, C = map(int, input().split())
map = [list(map(str, input())) for _ in range(R)]
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
visited = [[0]*C for _ in range(R)]

q = deque()

for i in range(R) :
    for j in range(C) :
        if map[i][j] == 'S' :
            q.append((i,j))      
        elif map[i][j] == 'D' :
            Dx, Dy = i, j

for i in range(R) :
    for j in range(C) :
        if map[i][j] == '*' :
            q.append((i,j))

print(bfs(Dx,Dy))