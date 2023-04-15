import sys
A, B, C = map(int, sys.stdin.readline().split())

def square(x, y, z) :
    if y == 1:
        return x % z
    elif y % 2 == 0 :
        return((square(x, y//2, z)**2)%z)
    else :
        return(((square(x, y//2, z)**2)*x)%z)
    
print(square(A, B, C))
