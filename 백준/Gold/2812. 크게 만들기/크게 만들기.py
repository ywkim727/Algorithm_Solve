import sys

N, K = map(int, sys.stdin.readline().split())

num = sys.stdin.readline().rstrip()

stack = []

for i in num :
    while stack and K > 0 and stack[-1] < i :   #num에 있는 숫자를 stack에 넣고 다음 숫자와 비교, 다음 숫자가 stack에 있는 수보다 크면
        stack.pop()                             #stack[-1]에 더 큰 수가 나올때까지 pop을 하면서 다음 숫자를 앞에 배치 
        K -= 1
    stack.append(i) 

if K > 0 :                                      #만약 숫자를 덜 지웠다면 (숫자가 내림차순으로 주어진경우 ex:654321)
    print(''.join(stack[:N-K]))                 #뒤의 숫자를 남은 k개 만큼 지우고 출력 (하나도 못지우고 k=3인채로 내려올 테니까 K만큼 지우고 654출력)
else :
    print(''.join(map(str,stack)))
    
        
        
