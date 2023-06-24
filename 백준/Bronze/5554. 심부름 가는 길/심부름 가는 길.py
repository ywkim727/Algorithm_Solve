num = []
for _ in range(4) :
    num.append(int(input()))
x = sum(num) // 60
y = sum(num) % 60

print(x)
print(y)