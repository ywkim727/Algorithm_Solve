import sys
N, M = map(int, sys.stdin.readline().split())

num = list(map(int, sys.stdin.readline().split()))

left = 0
right = 0
count = 0

while right < N :
    res = sum(num[left:right+1])
    if res == M :
        count += 1
        right += 1
    elif res > M :
        left += 1
    elif res < M :
        right += 1

print(count)