import sys
N, M = map(int,sys.stdin.readline().split())

no_hear = []
no_see = []

for _ in range(N) :
    no_hear.append(sys.stdin.readline())

for _ in range(M) :
    no_see.append(sys.stdin.readline())

result = list(set(no_hear)&set(no_see))

result.sort()

print(len(result))
print(''.join(result))