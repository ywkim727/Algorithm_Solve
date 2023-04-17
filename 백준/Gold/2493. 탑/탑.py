import sys

N = int(sys.stdin.readline())

tower = list(map(int, sys.stdin.readline().split()))

stack = []
answer = []

for i in range(N) :                         # 앞에서부터 순차적으로 탐색한다
    while stack :                           # 스택이 비어있지 않으면
        if stack[-1][1] > tower[i] :        # 탑이 신호를 수신할 수 있는지(탐색한 현재 탑의 높이가 스택에 가장 높이 있는 탑보다 작을때)
            answer.append(stack[-1][0] + 1) # 수신 받는 탑의 인덱스+1(0부터 시작하니까)를 answer에 넣어준다
            break
        else :                              # 현재 탑의 높이가 더 높아 수신할 수 없다면
            stack.pop()                     # 앞의 높이가 낮은 탑은 필요가 없으니 지워준다
    if not stack :                          # 스택이 비어있다면
        answer.append(0)                    # 신호를 받을 수 있는 탑이 없다 -> 0 
    stack.append([i, tower[i]])             # 스택에 인덱스와 탑의 높이를 튜플 형태로 저장

print(' '.join(map(str, answer)))