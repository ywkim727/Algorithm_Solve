x, y = map(int, input().split())

cut = int(input())

x_list = [0, x]
y_list = [0, y]

for _ in range(cut) :  
    cut_dir, cut_num = map(int, input().split())
    if cut_dir == 0 : #가로
        y_list.append(cut_num)
    elif cut_dir == 1 : #세로
        x_list.append(cut_num)

x_list.sort()
y_list.sort()

max_x = 0
max_y = 0

result_x = []
result_y = []

for i in range(len(x_list)-1) :
    A = x_list[i+1] - x_list[i]
    result_x.append(A)
    i += 1

for i in range(len(y_list)-1) :
    A = y_list[i+1] - y_list[i]
    result_y.append(A)
    i += 1

print(max(result_x)*max(result_y))

    
