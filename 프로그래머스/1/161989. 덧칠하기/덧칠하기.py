def solution(n, m, section):
    answer = 1
    target = section[0]
    for i in range(1, len(section)) :
        if section[i] - target >= m :
            answer += 1
            target = section[i]
    return answer