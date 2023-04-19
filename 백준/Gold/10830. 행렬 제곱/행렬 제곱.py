import sys

def multiple (n,matrix1, matrix2) :                             #행렬 곱셈 함수
    result = [[0 for _ in range(n)] for _ in range(n)]
    
    for i in range(N) :
        for j in range(N) :
            for k in range(N) :
                result[i][j] += matrix1[i][k] * matrix2[k][j]
            result[i][j] %= 1000
    return result
        
def divide(n, matrix, b) :
    if b == 1 :
        return matrix
    elif b == 2 :
        return (multiple(n, matrix, matrix))
    else :
        temp = divide(n, matrix, b//2)
        if b % 2 == 0 :
            return multiple(n, temp, temp)
        else :
            return multiple(n, multiple(n, temp, temp), matrix)


N, B = map(int, sys.stdin.readline(). split())

Matrix = [list(map(int, sys.stdin.readline(). split())) for _ in range(N)]

answer = divide(N, Matrix, B)

for row in answer :
    for num in row :
        print(num%1000, end=' ')        #마지막에도 모듈러 연산을 해줘야 한다, 반례)b=1일때 1000이상 값이 들어올때
    print()


