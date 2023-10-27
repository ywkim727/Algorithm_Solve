def solution(quiz):
    answer = []
    for i in quiz :
        i = i.split('=')
        q = i[0].split()
        res = int(q[0])
        if q[1] == '+' :
            res += int(q[2])
        elif q[1] == '-' :
            res -= int(q[2])
        
        if res == int(i[1]) :
            answer.append("O")
        else :
            answer.append("X")
        
    return answer