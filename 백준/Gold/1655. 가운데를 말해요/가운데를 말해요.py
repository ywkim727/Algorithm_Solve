import sys
from heapq import heappush, heappop

N = int(sys.stdin.readline())
left_h = []                                         #힙을 2개 쓴다
right_h = []                                        #left = max힙, right = min힙
                                                    #left와 right에 번갈아 값을 넣어주면서 균형을 맞추면 leftpop이 중간값이 된다
for _ in range(N) :
    num = int(sys.stdin.readline())
    if len(left_h) == len(right_h) :
        heappush(left_h, -num)                      
    else :
        heappush(right_h, num)                      
    if right_h and -left_h[0] > right_h[0] :        #right에 넣는 값이 left[0]보다 작은 값이면 서로 바꿔줘야 한다
        left_value = heappop(left_h)                #중간값보다 큰 값이 left[0]에 위치해 있기 때문에
        right_value = heappop(right_h)
        heappush(left_h, -right_value)
        heappush(right_h, -left_value)
    print(-left_h[0])


        