from collections import deque
M, N = map(int, input().split())
tomato = []
for i in range(N) :
    tomato.append(list(map(int, input().split())))

def bfs() :
    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]
    q = deque()
    for i in range(N) :                                     #q에 처음에 받은 토마토 위치를 append
        for j in range(M) :
            if tomato[i][j] == 1 :
                q.append([i,j])
    while q :
        x, y = q.popleft()                                  #처음 토마토 좌표 꺼내고
        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >= N or nx < 0 or ny >= M or ny < 0 :
                continue
            else :
                if tomato[nx][ny] == 0 :                    #탐색한 좌표에 토마토가 익지 않았으면
                    tomato[nx][ny] = tomato[x][y] + 1       #익히고 1을 더해주면서 횟수를 세어주기, 여기서 나온 제일 큰 값이 정답이 된다
                    q.append([nx, ny])
result = 0
bfs()
for i in tomato :
    for j in i :
        if j == 0 :                                         #다 찾아봤는데 토마토를 익히지 못했다면 -1출력
            print(-1)
            exit(0)        
    result = max(result, max(i))                            #다 익혔다면 최댓값이 정답

print(result-1)                                             #처음 시작을 1로 표현했으니 1을 빼준다