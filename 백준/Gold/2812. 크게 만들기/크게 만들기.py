import sys

N, K = map(int, sys.stdin.readline().split())

num = sys.stdin.readline().rstrip()

stack = []

for i in num :
    while stack and K > 0 and stack[-1] < i :
        stack.pop()
        K -= 1
    stack.append(i) 

if K > 0 :
    print(''.join(stack[:-K]))
else :
    print(''.join(map(str,stack)))
    
    
        
        