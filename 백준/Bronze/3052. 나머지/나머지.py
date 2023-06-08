num = []
for _ in range(10) :
    num.append(int(input()) % 42)

print(len(list(set(num))))