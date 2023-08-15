N = int(input())

for i in range(1, N+1) :
    new_i = list(str(i))
    res = i + sum(int(i) for i in new_i)
    if res == N :
        print(i)
        break
    if i == N :
        print(0)
