N = int(input())
M = int(input())
X = list(map(int, input().split()))

len_X = len(X)
min_height = 0

if len_X == 1 :                             #가로등이 1개밖에 없을 때
    min_height = max(X[0], N-X[0])          #왼쪽, 오른쪽 길이 중에 큰걸 선택 

for i in range(len_X) :
    if i == 0 :                             #맨 왼쪽에 있는 가로등
        height = X[i]                       #길이의 왼쪽 끝까지 비추면 된다
    elif i == len_X-1 :                     #맨 오른쪽에 있는 가로등
        height = N - X[i]                   #길이의 오른쪽 끝까지 비추면 된다
    else :                                  #중간에 있는 가로등
        temp = X[i] - X[i-1]                #그 앞에 있는 가로등과의 거리의 절반만 비추면 된다
        if temp % 2 :
            height = temp // 2 + 1
        else :
            height = temp // 2
    min_height = max(height, min_height)    #가장 넓은 범위를 비추는 가로등을 찾으면 된다

print(min_height)