import sys

def dfs(v) :
    ans_dfs.append(v)                   #방문 노드 추가
    visited[v] = 1                      #방문 표시
    
    for i in adj[v] :                   #인접한 노드 중에서
        if not visited[i] :             #방문하지 않은 노드면
            dfs(i)

def bfs(v) :
    q = []
    q.append(v)                         #q에 초기 데이터 삽입
    ans_bfs.append(v)
    visited[v] = 1

    while q :
        c = q.pop(0)
        for i in adj[c] :               #방문하지 않은 노드일 경우
            if not visited[i] :
                q.append(i)
                ans_bfs.append(i)
                visited[i] = 1


N, M, V = map(int, sys.stdin.readline().split())

adj = [[] for _ in range(N+1)]

for _ in range(M) :
    s, e = map(int, sys.stdin.readline().split())
    adj[s].append(e)
    adj[e].append(s)                                #양방향 연결

for i in adj :
    i.sort()                                        #각 노드 오름차순 정렬

visited = [0] * (N+1)
ans_dfs = []
dfs(V)

visited = [0] * (N+1)
ans_bfs = []
bfs(V)

print(*ans_dfs)
print(*ans_bfs)


