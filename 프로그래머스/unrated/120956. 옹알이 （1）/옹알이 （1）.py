def solution(babbling):
    answer = 0
    for i in babbling :
        word = ''
        for j in i :
            word += j
            if word in ['aya', 'ye', 'woo', 'ma'] :
                word = ''
        if len(word) == 0 :
            answer += 1
    return answer