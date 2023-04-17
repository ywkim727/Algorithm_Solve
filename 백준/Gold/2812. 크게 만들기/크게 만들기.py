import sys

N, K = map(int, sys.stdin.readline().split())

num = sys.stdin.readline().rstrip()

stack = []

for i in num :
    while stack and K > 0 and stack[-1] < i :   #num에 있는 숫자를 stack에 넣고 다음 숫자와 비교, 다음 숫자가 stack에 있는 수보다 크면
        stack.pop()                             #stack[-1]에 더 큰 수가 나올때까지 pop을 하면서 다음 숫자를 앞에 배치 
        K -= 1
    stack.append(i) 

if K > 0 :                                      #만약 숫자를 덜 지웠다면
    print(''.join(stack[:N-K]))                 #뒤의 숫자를 남은 k개 만큼 지우고 출력
else :
    print(''.join(map(str,stack)))
    
        
        
