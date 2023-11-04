def solution(num, total):

    start = total // num 
    
    for i in range(num) :
        result = range(start - i, start - i + num)
        if sum(result) == total :
            return list(result)