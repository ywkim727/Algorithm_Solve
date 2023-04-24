import sys
from collections import deque

N, M  = map(int, sys.stdin.readline().split())

graph = []

for _ in range(N) :
    graph.append(list(map(int, sys.stdin.readline().strip())))

def bfs(x, y) :
    dx = [0,0,1,-1]                                                     #상하좌우
    dy = [1,-1,0,0]

    q = deque()
    q.append((x, y))

    while q :
        x, y = q.popleft()
        for i in range(4) :                                            #동서남북을 검사하여 이동할 수 있는 칸을 찾는다
            nx = x + dx[i]
            ny = y + dy[i]

            if nx >= N or nx < 0 or ny >= M or ny < 0 :
                continue
            if graph[nx][ny] == 0 :
                continue
            if graph[nx][ny] == 1 :                                    #이동 할 수 있는 칸이라면 그 전 값에 +1해주어 최소 칸 수를 더해줌
                q.append((nx, ny))
                graph[nx][ny] = graph[x][y] + 1
    return graph[N-1][M-1]                                             #graph가 0,0(원래는 1,1) 부터 시작하기 때문에 최종은 N-1,M-1

print(bfs(0,0))        

# 참고로 소스코드 상에서 첫 번째 시작 위치가 다시 방문할 수 있도록 되어서 graph[0][0] 값이 3으로 바뀌었다.
# 그러나 이 문제에서는 단순히 가장 오른쪽 아래 위치로 이동하는 것을 요구하고 있기 때문에 답을 도출하는 데에는 문제가 없다.