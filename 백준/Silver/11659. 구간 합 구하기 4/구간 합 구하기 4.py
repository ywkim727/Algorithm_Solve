import sys
N, M = map(int, sys.stdin.readline().split())
num = list(map(int, sys.stdin.readline().split()))

total = 0
sum_list = [0]

for i in range(len(num)) :                          #sum_list는 누적합
    total += num[i]
    sum_list.append(total)

for _ in range(M) :
    i, j = map(int, sys.stdin.readline().split())
    print(sum_list[j]-sum_list[i-1])