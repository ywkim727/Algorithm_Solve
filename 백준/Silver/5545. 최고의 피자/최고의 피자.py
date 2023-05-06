N = int(input())

A, B = map(int, input().split())

C = int(input())

topping = []                         

for _ in range(N) :
    topping.append(int(input()))

topping.sort(reverse=True)              #토핑을 내림차순으로 정렬

answer = C / A                         #토핑을 하나도 안 올릴 경우도 생각해야 한다

for i in range(1, len(topping)+1) :
    cal = C + sum(topping[:i])
    cost = A + B * len(topping[:i])
    if cal / cost > answer :
        answer = cal / cost
    else :
        break

print(int(answer))