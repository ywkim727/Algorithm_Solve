# '-' 기준으로 괄호를 친다
num = input().split('-')    # '-' 기준으로 split해서 리스트에 저장

result = []                 #'-'로 나눈 항들의 합을 저장할 리스트
for i in num :
    sum = 0
    b = i.split('+')        # 덧셈을 하기 위해 '+' 기준으로 split
    for j in b :            # split한 리스트의 각 요소를 더해줌
        sum += int(j)   
    result.append(sum)      # 각 항의 덧셈 결과를 저장

start = result[0]           

for i in range(1, len(result)) :    #0번째 값에서 나머지들을 빼준다
    start -= result[i]

print(start)