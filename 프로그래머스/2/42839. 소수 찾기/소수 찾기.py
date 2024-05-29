import itertools

def solution(numbers):
    num_list = list(numbers)
    arr = []
    for i in range(1, len(num_list) + 1) :
        arr += list(itertools.permutations(num_list, i))
    
    new_nums = [int(("").join(p)) for p in arr]
              
    #소수 판별
    answer = []
    for i in new_nums :
        check = True
        if i < 2 :
            continue
        for j in range(2, int(i**0.5)+1) :
            if i % j == 0 :
                check = False
                break
        if check == True :
            answer.append(i)
    return len(set(answer))
        
            
            