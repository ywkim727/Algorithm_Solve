case = int(input())

for i in range(case) :
    quiz = list(input())
    score = 0
    add = 0
    for j in quiz :
        if j == 'O' :
            add += 1
        elif j == 'X' :
            add = 0
        score += add
    print(score)
        


