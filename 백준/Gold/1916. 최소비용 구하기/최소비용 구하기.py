import sys
from heapq import heappop, heappush
#다익스트라 알고리즘 풀이
def dijkstra(start, end) :
    distance = [int(1e9)] * (N+1)
    heap = []
    heappush(heap, (0, start))
    distance[start] = 0

    while heap :
        weight, index = heappop(heap)
        if distance[index] < weight :   #큐에서 뽑아낸 거리가 이미 갱신된 거리보다 클 경우(=방문함 셈) 무시
            continue
        for e, c in bus[index] :
            if distance[e] > weight + c :
                distance[e] = weight + c
                heappush(heap,(weight+c, e))
    return distance[end]

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())

bus = [[] for _ in range(N+1)]
for _ in range(M) :
    s, e, cost = map(int, sys.stdin.readline().split())
    bus[s].append((e, cost))

start, end = map(int, sys.stdin.readline().split())
print(dijkstra(start, end))
