def solution(cards1, cards2, goal):
    answer = 'Yes'
    
    idx1, idx2 = 0, 0
    
    for i in goal :
        if idx1 < len(cards1) and i == cards1[idx1] :
            idx1 += 1
        elif idx2 < len(cards2) and i == cards2[idx2] :
            idx2 += 1
        else :
            answer = "No"
            break
            
    
    return answer