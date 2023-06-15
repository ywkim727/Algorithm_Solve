plus, minus = map(int, input().split())

 
if minus > plus :
    print(-1)
elif (plus + minus) % 2 :
    print(-1)
else :
    a = (plus + minus)//2
    b = plus - a
    print(a, b)