def solution(answers):
    supo_ans = [
        [1,2,3,4,5],
        [2,1,2,3,2,4,2,5],
        [3,3,1,1,2,2,4,4,5,5]
    ]
    scores = [0,0,0]
    
    for su_idx, su_ans in enumerate(supo_ans) :
        for idx, ans in enumerate(answers) :
            if ans == su_ans[idx%len(su_ans)] :
                scores[su_idx] += 1
    
    return [idx+1 for idx, score in enumerate(scores) if max(scores) == score]