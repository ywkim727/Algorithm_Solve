N = int(input())

def fac(num) -> int :
    if num > 0 :
        return num * fac(num-1)
    else :
        return 1

print(fac(N))
