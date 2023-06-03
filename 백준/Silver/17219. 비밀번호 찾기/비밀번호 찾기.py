import sys

N, M = map(int,sys.stdin.readline().split())

password = {}

for _ in range(N) :
    a, b = sys.stdin.readline().split()
    password[a] = b

for _ in range(M) :
    c = sys.stdin.readline().rstrip()
    print(password[c])


