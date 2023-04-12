def permutation(arr, n):    #순열 알고리즘
    result = []
    if n == 0:
        return [[]]
    
    for i in range(len(arr)):
        elem = arr[i]
        for rest in permutation(arr[:i] + arr[i+1:], n - 1):
            result.append([elem] + rest)
    return result

N = int(input())

num_list = list(map(int, input().split()))
per_list = list(permutation(num_list, N))
                       
def max_num(list) :  #  차이의 최댓값을 구하기, 합계가 result보다 높으면 result값 갱신
    result = 0
    for i in list :
        sum = 0
        for j in range(len(i)-1) :
            sum += abs(i[j] - i[j+1])
            if result < sum :
                result = sum
    return result

print(max_num(per_list))
