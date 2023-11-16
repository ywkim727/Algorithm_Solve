def solution(array):
    
    max_i = 0
    max_n = 0
    
    for idx, num in enumerate(array) :
        if max_n < num :
            max_n = num
            max_i = idx
    
    return [max_n, max_i]