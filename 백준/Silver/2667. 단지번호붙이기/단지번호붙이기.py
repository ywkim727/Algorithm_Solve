from collections import deque
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

def bfs(graph, a, b) :
    graph[a][b] = 0                        #1인 부분은 0으로 바꿔 다시 방문 안하도록 함
    q = deque()
    q.append((a,b))
    count = 1
    while q :
        x, y = q.popleft()
        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= N :
                continue
            if graph[nx][ny] == 1 :
                graph[nx][ny] = 0
                q.append((nx, ny))
                count += 1

    return count

N = int(input())

graph = [list(map(int, input().rstrip())) for _ in range(N)]

count = []

for i in range(N) :
    for j in range(N) :
        if graph[i][j] == 1 :               #그래프의 탐색 시작점을 모르기 때문에 1인 지점을 찾아서 탐색을 시작
            count.append(bfs(graph,i,j))

count.sort()

print(len(count))
for i in count :
    print(i)