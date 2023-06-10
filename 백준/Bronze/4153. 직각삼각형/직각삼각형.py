while(1) :
    num = list(map(int,input().split()))
    num.sort()
    A = int(num[0])
    B = int(num[1])
    C = int(num[2])
    if (A == 0 and B == 0 and C == 0) :
        break
    elif (A*A + B*B == C*C) :
        print('right')
    else :
        print('wrong')