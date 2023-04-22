import sys 
sys.setrecursionlimit(10**7)
def dfs(v) :
    for i in adj[v] :
        if not visited[i] :                 #dfs는 무조건 부모에서 자식노드로 이동한다
            visited[i] = v                  #방문한 노드에 부모 노드 값을 저장한다, visited에 0이 아닌 수가 저장이 되기 때문에 다시 방문하지 않는다
            dfs(i)

N = int(sys.stdin.readline())

adj = [[] for _ in range(N+1)]

for _ in range(N-1) :
    s, e = map(int, sys.stdin.readline().split())
    adj[s].append(e)
    adj[e].append(s)

visited = [0] * (N+1)

dfs(1)

for i in range(2, N+1) :
    print(visited[i])