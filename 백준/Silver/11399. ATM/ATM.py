N = int(input())
people = list(map(int, input().split()))

people.sort()
max_sum = 0

for i in range(len(people)):
    max_sum += sum(people[:i+1])
    
print(max_sum)