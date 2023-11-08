def solution(chicken):
    answer = 0
    
    while True :
        coupon = chicken // 10
        chicken -= coupon * 9
        answer += coupon
        
        if not coupon :
            break
    
    return answer