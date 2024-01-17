import collections

def solution(participant, completion):
    result = collections.Counter(participant) - collections.Counter(completion)
    return list(result.keys())[0] #딕셔너리의 키 값 갖고오기
            