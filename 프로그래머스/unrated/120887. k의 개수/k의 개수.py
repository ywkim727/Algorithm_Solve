def solution(i, j, k):
    answer = 0
    
    for n in range(i, j+1) :
        n = list(str(n))
        for m in n :
            if m == str(k) :
                answer += 1
    
    return answer