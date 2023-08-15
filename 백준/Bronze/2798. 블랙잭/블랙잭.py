import itertools

N, M = map(int, input().split())
card = list(map(int, input().split()))

c_card = list(itertools.combinations(card, 3))

max_sum = 0
for i in c_card :
    if sum(i) > M :
        continue
    elif max_sum < sum(i) :
        max_sum = sum(i)

print(max_sum)
