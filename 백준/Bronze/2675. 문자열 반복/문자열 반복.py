T = int(input())

for _ in range(T) :
    P = []
    R, S = input().split()
    R = int(R)
    for i in S:
        P.append(i * R)
    print(''.join(P))
