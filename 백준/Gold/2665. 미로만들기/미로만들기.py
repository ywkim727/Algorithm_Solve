import sys
from heapq import heappop, heappush

def dijkstra(x, y) :                                            #(1,1)에서 출발하여 (N,N)까지 이동하는동안 비용(벽을부수는)을 구해야 한다
    dx = [0, 0, -1, 1]                                          #상하좌우를 탐색해서 벽이면 비용+1, 아니면 현재 비용 그대로를 힙에 추가한다
    dy = [1, -1, 0, 0]                                          #힙은 비용을 기준으로(비용기준의 최소힙) 다음 탐색할 위치가 나오게 된다        
    heap = []                                                   #방문한 곳은 표시를 해두어 다시 못가게 하면 결국 벽이 아닌곳만 우선으로 계속 방문하게 된다 (힙을 통해 계속해서 최소비용을 갖는 다음 탐색 위치가 나오게된다.)
    heappush(heap, (0, x, y))                                   #그러다 모두 방문했을 때 벽이 있는곳을 방문하게 된다 (비용 + 1)
    visited = [[0 for _ in range(N)] for _ in range(N)]         #현재 위치가 도착지일 때는 현재의 비용을 반환하도록 한다

    while heap :
        cost, x, y = heappop(heap)
        if x == N-1 and y == N-1 :
            return cost
        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >= N or nx < 0 or ny >= N or ny < 0 :
                continue
            elif visited[nx][ny] == 0 :
                visited[nx][ny] = 1
                if maze[nx][ny] == 1 :
                    heappush(heap, (cost, nx, ny))
                else :
                    heappush(heap, (cost+1, nx, ny))


N = int(sys.stdin.readline())

maze = []
for _ in range(N) :
    maze.append(list(map(int, sys.stdin.readline().strip())))

result = dijkstra(0,0)

print(result)