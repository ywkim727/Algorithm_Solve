from collections import defaultdict

def solution(survey, choices):
    result = defaultdict(int)
    for sur, cho in zip(survey, choices) :
        if cho < 4 :
            result[sur[0]] += 4 - cho
        else :
            result[sur[1]] += cho - 4
    answer = ''
    for typ1, typ2 in ("RT", "CF", "JM", "AN") :
        answer += typ1 if result[typ1] >= result[typ2] else typ2
    return answer