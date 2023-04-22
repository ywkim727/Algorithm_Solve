import sys
sys.setrecursionlimit(10**7)
def dfs(v) :                    
    visited[v] = 1                      #방문 표시
    
    for i in adj[v] :                   #인접한 노드 중에서
        if not visited[i] :             #방문하지 않은 노드면
            dfs(i)

N, M = map(int, sys.stdin.readline().split())

adj = [[] for _ in range(N+1)]

for _ in range(M) :
    u, v = map(int, sys.stdin.readline().split())
    adj[u].append(v)
    adj[v].append(u)

visited = [0] * (N+1)

count = 0

for i in range(1, N+1) :
    if not visited[i] :
        visited[i] = 1
        count += 1
        dfs(i)

print(count)