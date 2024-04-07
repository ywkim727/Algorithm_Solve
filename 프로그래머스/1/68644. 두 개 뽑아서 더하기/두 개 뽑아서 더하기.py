import itertools 

def solution(numbers):
    
    answer = []
    
    com = list(itertools.combinations(numbers, 2))
    
    for i in com :
        hap = int(i[0]) + int(i[1])
        if hap not in answer :
            answer.append(hap)
            
    answer.sort()
    
    return answer