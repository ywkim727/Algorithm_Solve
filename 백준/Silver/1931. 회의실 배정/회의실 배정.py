# 1. 회의 시작 시간으로 오름차순 
# 2. 1 의 결과에서 끝나는 시간으로 다시 오름차순
import sys
N = int(sys.stdin.readline())

time = []

for _ in range(N) :
    start, end = map(int, sys.stdin.readline().split())
    time.append((start, end))

time.sort(key=lambda x : x[0])
time.sort(key=lambda x : x[1])

count = 0
last = 0

for i, j in time :
    if i >= last :
        last = j
        count += 1

print(count)