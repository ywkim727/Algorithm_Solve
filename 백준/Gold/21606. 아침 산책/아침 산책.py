import sys
sys.setrecursionlimit(10**7)
                                                           #실외노드를 기준으로 인접해있는 실내 노드를 카운트
def dfs(v, count) :
    visited[v] = 1

    for i in adj[v] :                                       #노드 v와 연결된 노드를 하나씩 탐색
        if not visited[i] and node[i] == 0:                 #인접한 노드가 방문하지 않은 실외 노드 이면 
            count = dfs(i, count)                           #dfs로 타고 들어가기
        elif node[i] == 1 :                                 #실내노드이면 count + 1
            count += 1
    return count

N = int(sys.stdin.readline())

node = [0] + list(map(int, sys.stdin.readline().strip()))   #노드의 정보(실내,실외) 앞에 [0]을 넣어주는 이유는 1번 인덱스부터 쓰기 위함

visited = [0] * (N+1)

adj = [[] for _ in range(N+1)]
ans = 0

for _ in range(N-1) :
    s, e = map(int, sys.stdin.readline().split())
    adj[s].append(e)
    adj[e].append(s)
    if node[s] == 1 and node[e] == 1 :                      #둘 다 실내 노드이면 경우의 수 +2 (서로 방문하는 케이스가 2가지니까)
        ans += 2
                                                            
sum = 0

for i in range(1, N+1) :
    if not visited[i] and node[i] == 0 :                    #방문하지 않은 실외노드이면
        x = dfs(i,0)                                        #주변의 실내노드를 dfs (현재 카운트는 0)
        sum += x*(x-1)                                      #경우의 수는 연결된 실내노드의 갯수n -> n(n-1)

print(sum + ans) 
