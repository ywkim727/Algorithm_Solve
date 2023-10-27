def solution(my_string, num1, num2):
    # 문자열은 불변한 타입이므로 리스트로 변환 후 인덱스를 바꿔준 후 다시 문자열로 변환한다
    answer = list(my_string)
    
    answer[num1], answer[num2] = answer[num2], answer[num1]
    
    
    return ''.join(answer)