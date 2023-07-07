N, M = map(int, input().split())

res = []

A = list(map(int, input().split()))
B = list(map(int, input().split()))

for i in A :
    B.append(i) 

B.sort()

for i in B :
    print(i, end=' ')