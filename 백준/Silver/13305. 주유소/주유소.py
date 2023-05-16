N = int(input())

roads = list(map(int, input().split()))
price = list(map(int, input().split()))

min_cost = price[0] * roads[0]

min_price = price[0]
for i in range(1, N-1) :
    if min_price > price[i] :
        min_price = price[i]

    min_cost += min_price * roads[i]
    
print(min_cost)