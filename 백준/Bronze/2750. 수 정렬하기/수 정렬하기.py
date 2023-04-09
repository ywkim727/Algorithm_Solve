#버블정렬 알고리즘

case = int(input())

num_list = []

for _ in range(case) :
    num = int(input())
    num_list.append(num)

n = len(num_list)

for i in range(n-1) :
    for j in range(n-1, i, -1) :
        if num_list[j-1] > num_list[j] :
            num_list[j-1], num_list[j] = num_list[j], num_list[j-1]

for i in num_list :
    print(i)
