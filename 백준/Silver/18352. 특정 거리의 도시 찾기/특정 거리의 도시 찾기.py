import sys
from collections import deque

def bfs(v) :
    q = deque()
    q.append(v)
    visited[v] = 1
    distance[v] = 0
    while q :
        c = q.popleft()
        for i in adj[c] :
            if visited[i] == 0 :
                q.append(i)
                visited[i] = 1
                distance[i] = distance[c] + 1                
                if distance[i] == K :
                    answer.append(i)

N, M, K, X = map(int, sys.stdin.readline().split())

adj = [[] for _ in range(N+1)]
visited = [0] * (N+1)
distance = [0] * (N+1)

for _ in range(M) :
    A, B = map(int, sys.stdin.readline().split())
    adj[A].append(B)

answer = []
bfs(X)

if not answer :
    print(-1)
else :
    answer.sort()
    for i in answer :
        print(i)