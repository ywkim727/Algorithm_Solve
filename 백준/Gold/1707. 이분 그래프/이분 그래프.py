#이분 그래프란? : 인접한 정점끼리 서로 다른 색으로 칠해서 모든 정점을 두가지의 색으로만 칠할 수 있는 그래프 
#현재 노드와 이웃한 노드의 색을 확인, 동일한 색이 칠해져 있다면 이분그래프가 아닌 것으로 판단
import sys 
sys.setrecursionlimit(10**7)

K = int(sys.stdin.readline())

def dfs(v) :
    global result

    for i in adj[v] :                           #인접한 노드 탐색
        if visited[i] == 0 :                    #이웃 노드에 색이 칠해져 있지 않을때
            if visited[v] == 1 :                #현재 노드의 색이 1이면 이웃노드는 2로 칠하고 2이면 1로 칠하기
                visited[i] = 2          
            elif visited[v] == 2 :      
                visited[i] = 1
            dfs(i)                              #dfs 통해 반복
        else :                                  #이웃 노드에 색이 이미 칠해져 있을때
            if visited[i] == visited[v] :       #현재 노드와 이웃 노드의 색이 같다면 
                result = False              
                return


for _ in range(K) :
    V, E = map(int, sys.stdin.readline().split())

    adj = [[] for _ in range(V+1)]
    visited = [0] * (V+1)                       #색칠 여부 저장

    for _ in range(E) :
        u, v = map(int, sys.stdin.readline().split())
        adj[u].append(v)
        adj[v].append(u)

    result = True                               #초기 result = Ture

    for i in range(1, V+1) :                    #모든 노드의 탐색을 진행
        if visited[i] == 0 :                    #현재 노드에 색이 칠해져 있지 않으면
            visited[i] = 1                      #색을 칠하고
            dfs(i)                              #이웃 노드를 탐색
            if result == False :                #이분 그래프가 아님으로 드러나면 
                break                           #바로 종료

    if result == True :                         #result == True면 이분그래프, False면 이분그래프 아님
        print('YES')
    else :
        print('NO')