num = list(map(int, input()))

count = 0

for i in range(len(num)) :
    if num[i] != num[i-1] :
        count += 1

print(count//2)