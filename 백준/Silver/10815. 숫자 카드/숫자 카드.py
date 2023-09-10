N = int(input())
N_list = list(map(int, input().split()))
N_arr = sorted(N_list)
M = int(input())
M_list = list(map(int, input().split()))
res = []

def b_search(arr, target) :
    s = 0
    e = len(arr)-1

    while True :
        m = (s+e)//2
        if target > arr[m] :
            s = m + 1
        elif target < arr[m] :
            e = m - 1
        elif target == arr[m] :
            return 1
        
        if s > e :
            return 0
        

for i in M_list :
    res.append(b_search(N_arr, i))

for i in res :
    print(i, end=' ')