T = int(input())

for i in range(T) :
    count = 0
    vps = list(map(str, input()))
    for i in vps :
        if i == '(' :
            count += 1
        elif i == ')' :
            count -= 1
        if count < 0 :
            print('NO')
            break
    if count > 0 :
        print('NO')
    elif count == 0 :
        print('YES')

