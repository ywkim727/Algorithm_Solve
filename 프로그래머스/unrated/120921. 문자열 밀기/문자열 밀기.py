def solution(A, B):
    answer = 0
    count = 0
    if A == B :
        return 0
    else :
        for _ in range(len(A)) :
            temp = A[-1] + A[:-1]
            count += 1
            if temp == B :
                break
            else :
                A = temp
        if count == len(A) :
            answer = -1
        else :
            answer += count
    return answer