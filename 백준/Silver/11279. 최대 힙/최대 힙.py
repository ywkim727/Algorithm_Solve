from heapq import heappop, heappush
import sys
N = int(sys.stdin.readline())

num = []

for _ in range(N) :
    command = int(sys.stdin.readline())
    if command == 0 :
        if len(num) == 0 :
            print(0)
        else :
            print(heappop(num)[1])
    else :
        heappush(num, (-command, command))