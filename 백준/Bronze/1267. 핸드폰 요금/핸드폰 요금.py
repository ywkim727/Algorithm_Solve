n = int(input())
num = list(map(int, input().split()))
Y = []
M = []
for i in num :
    y = ((i//30)+1) * 10
    Y.append(y)
    m = ((i//60)+1) * 15
    M.append(m)

if sum(Y) == sum(M) :
    print("Y", "M", sum(Y))
elif sum(Y) > sum(M) :
    print("M", sum(M))
else :
    print("Y", sum(Y))