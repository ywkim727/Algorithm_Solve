import sys
T = int(sys.stdin.readline())

for _ in range(T) :
    score = []
    N = int(sys.stdin.readline())
    for _ in range(N) :
        s, m = map(int, sys.stdin.readline().split())
        score.append((s,m))
    score.sort(key = lambda x : x[0])
    count = 1
    min = score[0][1]
    for i in range(N) :
        if score[i][1] < min :
            min = score[i][1]
            count += 1
    print(count)