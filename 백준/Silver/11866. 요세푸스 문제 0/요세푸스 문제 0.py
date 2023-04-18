import sys
from collections import deque

N, K = map(int, sys.stdin.readline().split())
circle = deque()

for i in range(1, N+1) :
    circle.append(i)

print('<', end='')

while circle :
    for i in range(K-1) :
        circle.append(circle[0])
        circle.popleft()
    print(circle.popleft(), end='')
    if circle :
        print(', ', end='')
print('>')

# 입력받은 k번째까지 요소를 없애고, 그 요소들을 뒤에 추가해준다.

# k번째 숫자를 출력해주고 그 요소를 없애준다.

# 요소가 없어질때 까지 반복해준다.
