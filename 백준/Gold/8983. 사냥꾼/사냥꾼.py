import sys
M, N, L = map(int, sys.stdin.readline().split())
X = list(map(int, sys.stdin.readline().split()))
animal = list(map(int, sys.stdin.readline().split()) for _ in range(N))

X.sort()

count = 0

for x, y in animal :                        #동물의 위치를 고정하고 사냥 가능한 사대의 위치를 탐색
    if y > L :                              #y>L이면 무조건 사정거리를 벗어나므로 패스
        continue
    left = 0
    right = M-1                             #사대 리스트X의 인덱스가 0~3 이기 때문에 left=0 ~ right=M-1로 설정
    s = x + y - L                           #최소 사정거리 s = x+y-L, 최대 사정거리 e = x-y+L
    e = x - y + L
    while left <= right :                   #이분탐색 시작
        mid = (left + right) // 2
        if X[mid] >= s and X[mid] <= e :    #중간값 mid 기준으로 X[mid]가 사정거리 안에 들어오면 count++
            count += 1
            break
        elif X[mid] > e :                   #사정거리보다 크면 더 작은 사대를 써야 하므로 인덱스 범위를 줄인다
            right = mid - 1
        elif X[mid] < s :                   #반대면 더 멀리있는 사대를 써야 하므로 인덱스 범위를 늘린다
            left = mid + 1
            
print(count)
