def solution(my_string):
    answer = 0
    word = ''
    for i in my_string :
        if i in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0'] :
            word += i
        else :
            if len(word) > 0 :
                answer += int(word)
                word = ''
            else :
                continue
    # 문자열 끝에 자연수가 있는 경우도 고려해야함
    if len(word) > 0 :
        answer += int(word)
    return answer