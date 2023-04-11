import sys
# 병합 정렬 알고리즘

def merge_sort(array):
    if len(array)<=1:
        return array
    mid = len(array) // 2
    left = merge_sort(array[:mid]) #배열을 2개로 나눠서 각각 정렬
    right = merge_sort(array[mid:])

    i,j,k = 0,0,0

    while i < len(left) and j <len(right):
        if left[i] < right[j]:
            array[k] = left[i]
            i += 1
        else:
            array[k] = right[j]
            j += 1
        k+=1
    
    if i==len(left):
        while j < len(right):
            array[k] = right[j]
            j += 1
            k += 1
    elif j==len(right):
        while i < len(left):
            array[k] = left[i]
            i += 1
            k += 1
    return array


N = int(sys.stdin.readline())
num_list = []

for i in range(N) :
    num_list.append(int(sys.stdin.readline())) 

num = merge_sort(num_list)

for i in num :
    print(i)