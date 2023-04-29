A = list(input())
B = list(input())

lenA = len(A)
lenB = len(B)
LCS = [[0] * (lenB + 1)for _ in range(lenA + 1)]

for i in range(1, lenA + 1) :
    for j in range(1, lenB + 1) :
        if A[i-1] == B[j-1] :
            LCS[i][j] = LCS[i-1][j-1] + 1
        else :
            LCS[i][j] = max(LCS[i][j-1], LCS[i-1][j])

print(LCS[-1][-1])