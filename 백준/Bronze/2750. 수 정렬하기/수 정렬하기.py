case = int(input())

num_list = []

for _ in range(case) :
    num = int(input())
    num_list.append(num)

num_list.sort()

for i in num_list :
    print(i)