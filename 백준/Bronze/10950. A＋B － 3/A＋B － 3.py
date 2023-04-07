case = int(input())

temp = [None] * case

for i in range(case) :
    A, B = map(int,input().split())
    temp[i]= A + B

for i in range(case) :
     print(temp[i])
