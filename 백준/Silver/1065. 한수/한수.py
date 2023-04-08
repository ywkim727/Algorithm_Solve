N = int(input())

def han(N) -> int :
    count = 0
    if N < 100 :
        count += N
    else : 
        count = 99 
        for i in range(100, N+1) :
            num = list(map(int, str(i)))
            if (num[1] - num[0]) == (num[2] - num[1]) :
                count += 1
    return count

print(han(N))


