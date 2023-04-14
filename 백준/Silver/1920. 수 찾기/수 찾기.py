import sys

def b_search(arr, target)->int :
    
    pl = 0
    pr = len(arr)-1
    
    while True:
        pc = (pl+pr)//2 

        if target > arr[pc] :
            pl = pc + 1
        elif target < arr[pc] :
            pr = pc -1
        elif target == arr[pc] :
            return 1
        
        if pl > pr :
            break
    return 0

N = int(input())
N_num = list(map(int, sys.stdin.readline().split()))
s_arr = sorted(N_num)

M = int(input())
M_num = list(map(int, sys.stdin.readline().split()))

for i in M_num :
    print(b_search(s_arr, i))