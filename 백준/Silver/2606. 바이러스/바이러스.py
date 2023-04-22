import sys

def dfs(v) :
    global count
    visited[v] = True
    count += 1
    for i in adj[v] :
        if not visited[i] :
            dfs(i)
         

N = int(sys.stdin.readline())

edge = int(sys.stdin.readline())

adj = [[] for _ in range(N+1)]

for _ in range(edge) :
    s, e = map(int, sys.stdin.readline().split())
    adj[s].append(e)
    adj[e].append(s)

visited = [0] * (N+1)
count = 0

dfs(1)

print(count-1)  #1은 빼고 세니까