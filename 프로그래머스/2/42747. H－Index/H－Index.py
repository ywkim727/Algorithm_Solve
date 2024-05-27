def solution(citations):
    li = sorted(citations)
    for i in range(len(li)) :
        if li[i] >= len(li) - i :
            return len(li) - i
    return 0
        