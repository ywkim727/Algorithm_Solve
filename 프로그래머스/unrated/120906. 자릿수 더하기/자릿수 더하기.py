def solution(n):
    answer = 0
    num = list(str(n))
    for i in num :
        answer += int(i)
    
    return answer