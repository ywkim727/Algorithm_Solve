case = int(input())

for i in range(case) :
    score = list(map(int,input().split()))
    average = sum(score[1:]) / score[0]
    count = 0
    for j in score[1:] :
        if average < j :
            count += 1
    result = count/score[0] * 100
    print(f'{result:.3f}%')
       
