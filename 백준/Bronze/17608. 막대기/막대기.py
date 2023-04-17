import sys

N = int(sys.stdin.readline())

stick = []
count = 1

for _ in range(N) :
    stick.append(int(sys.stdin.readline()))

max = stick[-1]

for i in range(len(stick)-1, -1, -1) :
    if max < stick[i] :
        count += 1
        max = stick[i]

print(count)

