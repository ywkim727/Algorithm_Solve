#이분탐색 알고리즘 사용
N, M = map(int, input().split())

t_list =list(map(int, input().split()))

def cut_tree(list, target)->int :   
    start = 0
    end = max(list)

    while start <= end :    #start가 end 넘어설 때 까지
        trees = 0
        mid = (start + end) // 2
        for i in list : # tree list 하나씩 꺼내서
            if i > mid :       # 높이보다 나무가 더 크면 자를 수 있음
                trees += i - mid
        if trees >= target :    #자른 나무들의 합이 M보다 크면(M보다 저 잘랐으면)
            start = mid + 1     #start값 이동
        elif trees < target :   #덜 잘랐으면
            end = mid - 1       #end값 이동
    return end

print(cut_tree(t_list, M))
