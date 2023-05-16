N = int(input())

roads = list(map(int, input().split()))
price = list(map(int, input().split()))
cost = price[0] * roads[0]
d = 0
m = price[0]
for i in range(1, N-1) :
    if price[i] < m :
        cost += m * d
        d = roads[i]
        m = price[i]
    else :
        d += roads[i]
    if i == N-2 :
        cost += m * d
    
print(cost)