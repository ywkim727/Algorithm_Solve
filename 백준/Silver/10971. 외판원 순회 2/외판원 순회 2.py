n = int(input())
W = [list(map(int, input().split())) for _ in range(n)]

answer = 1e9    #answer를 매우 큰 값으로 초기화, 초기값으로 설정한 값 이상의 어떤 값이 들어올 경우를 대비
visited = [False] * n   #방문 여부를 나타내는 리스트

def dfs(node, x, cost) :    #node : 현재 노드, x : 방문한 도시의 수,  cost : 현재까지 비용
    global answer   #answer를 전역변수로 명시

    if x == n : #모든 도시를 방문했을 경우
        if W[node][0] :
            answer = min(answer, cost + W[node][0]) #현재까지 비용 + 0으로 돌아가는 비용 더해서 answer 업데이트
        return 

    for next_node in range(1, n) :  
        if W[node][next_node] and not visited[next_node] :  #다음노드로 갈 수 있고(0이 아니고), 다음 노드가 방문한 적이 없는 곳이면
            visited[next_node] = True   #방문한 도시 수 증가
            dfs(next_node, x+1, cost + W[node][next_node])  #재귀적으로 dfs 호출
            visited[next_node] = False  #방문한 노드를 True로 두고 탐색을 진행하다 해당 경로에 해답이 없을 경우 다시 해당 노드를 False로 두는 것이 백트래킹의 핵심
                                        #따라서 다음 노드로 이동하기 전에 visited[next_node] = False 수행함으로써, 이전 상태로 되돌아가서 다른 경로로 탐색이 가능하게 한다
dfs(0, 1, 0)
print(answer)
