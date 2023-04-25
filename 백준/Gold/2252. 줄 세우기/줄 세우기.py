#위상정렬 알고리즘
from collections import deque

N, M = map(int, input().split())

graph = [[] for _ in range(N+1)]
inDegree = [0 for _ in range(N+1)]
q = deque()
answer = []

for _ in range(M) :
    a, b = map(int, input().split())
    graph[a].append(b)
    inDegree[b] += 1

for i in range(1, N+1) :
    if inDegree[i] == 0 :                   #진입차수가 0인 정점을 큐에 삽입
        q.append(i)

while q :                               
    temp = q.popleft()
    answer.append(temp)
    for i in graph[temp] :                  #큐에서 해당원소를 꺼내 연결된 간선을 모두 제거
        inDegree[i] -= 1
        if inDegree[i] == 0 :               #제거한 이후 진입차수 0인 정점을 다시 삽입
            q.append(i)

print(*answer, end=' ')