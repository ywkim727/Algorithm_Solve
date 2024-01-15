def solution(s):
    result = [-1 for _ in range(len(s))]
    order = {}
    for idx, word in enumerate(s) :
        if word in order :
            result[idx] = idx - order[word]
        order[word] = idx
    return result