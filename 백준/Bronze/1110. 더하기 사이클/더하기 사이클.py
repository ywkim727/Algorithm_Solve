answer = list(str(input()))

N = answer  # 입력받은 answer를 N에다 복사

count = 0   # 사이클의 길이

while 1:
    if len(N) == 1 :    # 주어진 수가 1보다 작다면
        N.append('0')   # 0을 붙여 두 자리 수로 만들고
    
    temp = list(str(int(N[0]) + int(N[1]))) # ex) N = ['2', '6']이면 temp = ['8']

    if len(temp) == 1:                      # temp가 한자릿수('8')이면
        new_num = list(N[1] + temp[0])   # N[1]('6') + temp[0]('8'), new_num = ['6','8']
        count += 1
        N = new_num                      # N을 new_num으로 업데이트하고 반복
    else :
        new_num = list(N[1] + temp[1])   #temp가 두자릿수일때 위랑 똑같이
        count += 1
        N = new_num                      

    if new_num == answer :               # 새로운 수 new_num이 answer랑 같으면 루프 탈출
        break

print(count)
