from itertools import combinations

height = []

for _ in range(9) :
    height.append(int(input()))

height.sort()

seven = list(combinations(height, 7)) #7개씩 조합을 만든다

sum_list = []

for i in seven :
    sum_list.append(sum(i)) #sum_list에 각 조합당 합을 저장

  
for j in range(len(sum_list)) :
    if sum_list[j] == 100 :
        for k in seven[j] :
            print(k)
        break
            
       

