A = int(input())
B = int(input())
C = int(input())

result = list(str(A*B*C))

count = list([0] * 10)



for i in result :
    if i == '0' :
        count[0] += 1
    elif i == '1' :
         count[1] += 1
    elif i == '2' :
        count[2] += 1
    elif i == '3' :
        count[3] += 1
    elif i == '4' :
        count[4] += 1
    elif i == '5' :
        count[5] += 1
    elif i == '6' :
        count[6] += 1
    elif i == '7' :
        count[7] += 1
    elif i == '8' :
        count[8] += 1
    elif i == '9' :
        count[9] += 1
        
for i in count :
    print(i)

    