import sys
from heapq import heappop, heappush

N = int(sys.stdin.readline())

card = []
answer = 0

for _ in range(N) :
    num = int(sys.stdin.readline())
    heappush(card, num)

while len(card) > 1 :                   #작은 수부터 2개씩 더해줘야 가장 효율적
    plus1 = heappop(card)
    plus2 = heappop(card)

    plus = plus1 + plus2 
    answer += plus
    heappush(card, plus)

print(answer)