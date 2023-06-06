N = int(input())

people = []

for _ in range(N) :
    weight, height = map(int, input().split())
    people.append((weight, height))

grade = []

for i in range(N) :
    k = 0
    for j in range(N) :
        if people[i][0] < people[j][0] and people[i][1] < people[j][1] :
            k += 1
    grade.append(k+1)

for i in grade :
    print(i, end=" ")