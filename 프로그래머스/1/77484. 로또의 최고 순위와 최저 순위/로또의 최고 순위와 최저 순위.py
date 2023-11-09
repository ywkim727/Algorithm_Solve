def solution(lottos, win_nums):
    answer = []
    
    z_count = 0
    w_count = 0
    
    for i in lottos :
        if i == 0 :
            z_count += 1
        elif i in win_nums :
            w_count += 1
    
    num = [6,6,5,4,3,2,1]
    answer.append(num[w_count+z_count])
    answer.append(num[w_count])
    
    return answer