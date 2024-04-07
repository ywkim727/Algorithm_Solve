def solution(numbers):
    answer = []
    
    for i in range(len(numbers)) :
        for j in range(i+1, len(numbers)) :
            hap = int(numbers[i]) + int(numbers[j])
            if hap not in answer :
                answer.append(hap)
                
    answer.sort()
    
    return answer