# 투 포인터 알고리즘 풀이
import sys

N = int(sys.stdin.readline())

arr = list(map(int, sys.stdin.readline().split()))
arr.sort()  # 정렬시킨 배열을 이용

left = 0
right = N-1
answer = abs(arr[left] + arr[right])
result = [arr[left], arr[right]]    # 양쪽에서부터 합한 값 비교

while left < right :
    sum = arr[left] + arr[right]

    if abs(sum) < answer :  # 최솟값을 업데이트
        answer = abs(sum)
        result = [arr[left], arr[right]]
        if answer == 0 :   # 합이 0이면 탈출
            break
    if sum < 0 :    # sum이 음수일때 0에 가깝기 위해 값을 키워야 하므로 left + 1
        left += 1
    else :  # 양수일때 0에 가깝기 위해 값을 줄여야 하므로  right - 1
        right -= 1

print(result[0], result[1])
    

    