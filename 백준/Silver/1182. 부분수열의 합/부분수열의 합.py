def combinations(arr, n) :  # combination 구하는 함수 (외웠음)
    result = []
    if n == 0:
        return [[]]
    for i in range(len(arr)) :
        elem = arr[i]
        for rest in combinations(arr[i+1:], n-1) :
            result.append([elem] + rest)
    return result

N, S = map(int, input().split())

num = list(map(int, input().split()))

count = 0

for i in range(1, N+1) :    
    new_num = list(combinations(num, i))   # 부분 수열 만들기(원소 수 i를 1부터 N까지 반복)
    for j in new_num :
        sum_num = sum(j)    # 만들어진 부분 수열의 원소 ex: (-7, -3) 를 sum 하여 sum_num에 저장
        if sum_num == S :   # sum_num이 S값과 같으면 count++
            count += 1

print(count)
    