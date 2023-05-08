def b_search(list, num) :           
    s = 0
    e = len(list)-1
    res = -1
    while s <= e :
        mid = (s+e) // 2
        if num <= list[mid] :
            e = mid-1
        elif num > list[mid] :
            res = mid
            s = mid+1  
    return res
                                                            #B에서 A의 한 요소 보다 작은 수 중 제일 큰 수의 인덱스를 찾는다
        

T = int(input())

for _ in range(T) :
    A, B = map(int, input().split())
    numA = list(map(int, input().split()))
    numB = sorted(list(map(int, input().split())))
    result = 0
    for a in numA :
        result += b_search(numB, a) + 1                     # +1을 해주는 이유는 리스트의 인덱스가 0부터 시작하기 때문에 숫자가 하나씩 덜 나오기 때문
    print(result)