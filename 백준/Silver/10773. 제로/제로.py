import sys

K = int(sys.stdin.readline())

list = []

for i in range(K):
    command = int(sys.stdin.readline())
    if command == 0 :
        list.pop()
    else :
        list.append(command)

print(sum(list))

