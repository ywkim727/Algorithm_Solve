import sys 
from collections import deque
N = list(sys.stdin.readline().rstrip())
N2 = deque()
cursor = len(N)       
num = int(input())
for _ in range(num) :
    command = list(sys.stdin.readline().split())
    if command[0] == 'P' :
        # N.insert(cursor, command[1])
        N.append(command[1])
        cursor += 1
    elif command[0] == 'L' :
        if cursor <= 0 :
            continue
        else :
            cursor -= 1
            N2.appendleft(N.pop(cursor))
    elif command[0] == 'D' :
        if len(N2) == 0:
            continue
        else :
            N.append(N2.popleft())
            cursor += 1
    elif command[0] == 'B' :
        if cursor <= 0 :
            continue
        else :
            cursor -= 1
            N.pop(cursor)


for i in N2 :
    N.append(i)

for i in N :
    print(i, sep="\n",end="")
