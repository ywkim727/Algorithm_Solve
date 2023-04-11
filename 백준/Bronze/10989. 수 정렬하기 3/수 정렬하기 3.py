#도수정렬 알고리즘
import sys
N = int(sys.stdin.readline()) 

lst = [0] * 10001

for i in range(N) :  #입력받은 수에 해당하는 인덱스에+1
    lst[int(sys.stdin.readline())] += 1

for j in range(10001) : #for문으로 돌리면서 0아닌 값들 순서대로 뽑아 출력
    if lst[j] != 0 :
        for _ in range(lst[j]) :
            print(j)



