def solution(babbling):
    answer = 0
    
    pros = ['aya', 'ye', 'woo', 'ma']
    for i in babbling :
        for j in pros :
            if j*2 in i :
                break
            i = i.replace(j, ' ')
        
        if len(i.strip()) == 0 :
            answer += 1
    
    return answer