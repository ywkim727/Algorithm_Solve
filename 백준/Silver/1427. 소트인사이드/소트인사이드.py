N = list(map(int, input().rstrip()))
N.sort(reverse=True)

for i in N :
    print(i,end='')