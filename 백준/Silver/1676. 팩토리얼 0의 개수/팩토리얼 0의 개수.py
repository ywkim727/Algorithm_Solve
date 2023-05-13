N = int(input())

def fac(n) :
    if n == 0:
        return 1
    return n * fac(n-1)

num = list(str(fac(N)))
count = 0

for i in reversed(range(len(num))) :
    if num[i] != '0' :
        break
    elif num[i] == '0' :
        count += 1

print(count)