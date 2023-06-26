from collections import deque
N = int(input())
card = deque()
res = []
for i in range(1, N+1) :
    card.append(i)

while(len(card) > 1) :
    a = card.popleft()
    res.append(a)
    b = card.popleft()
    card.append(b)
    
res.append(card.pop())
for i in res :
    print(i, end=' ')