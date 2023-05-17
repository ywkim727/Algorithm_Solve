N = int(input())

case = []

for _ in range(N) :
    num, loc = map(int, input().split())
    case.append((num, loc))

case.sort(key = lambda x : x[0])

count = 0

for i in range(1, N) :
    if case[i][0] == case[i-1][0] :
        if case[i][1] != case[i-1][1] :
            count += 1

print(count)