import itertools

N = int(input())

N_list = []

for i in range(N, 0, -1) :
    N_list.append(i)

C_list = list(itertools.permutations(N_list, N))

C_list.sort()

for i in C_list :
    for j in i :
        print(j, end=' ')
    print(sep='\n')