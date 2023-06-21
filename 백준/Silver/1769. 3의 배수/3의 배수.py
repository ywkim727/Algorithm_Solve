import sys
N = int(sys.stdin.readline())
count = 0
if N > 10 :
    while(N >= 10) :
        num = list(map(int, (str(N))))
        N = sum(num)
        count += 1
print(count)
if N % 3 :
    print('NO')
else :
    print('YES')