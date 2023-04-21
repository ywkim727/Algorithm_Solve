#크루스칼 알고리즘을 통한 MST 구현
import sys
V, E = map(int, sys.stdin.readline().split())

edge = []

for _ in range(E) :
    A, B, C = map(int, sys.stdin.readline().split())
    edge.append((C, A, B))

edge.sort()                                                 #가중치 순으로 정렬

parent = [i for i in range(V+1)]                            #파인드-유니온 알고리즘 

def find_parent(x) :            
    if parent[x] == x :                                     #부모노드 == 자식노드 -> x 리턴
        return x
    else :
        parent[x] = find_parent(parent[x])                  #부모노드와 자식노드가 같지 않다면 재귀적으로 올라가서 parent갱신 
        return parent[x]

def union (a, b) :
    a = find_parent(a)
    b = find_parent(b)
    if a > b :                                              #작은쪽이 부모가 된다
        parent[a] = b
    else :
        parent[b] = a

def same_parent(a, b) :
    return find_parent(a) == find_parent(b)

answer = 0

for cost, a, b in edge :
    if not same_parent(a, b) :
        union(a, b)
        answer += cost

print(answer)
    