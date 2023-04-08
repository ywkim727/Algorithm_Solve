#골드바흐 파티션 : 2 이상의 모든 짝수는 두가지 소수의 합으로 나타낼 수 있다
case = int(input())
num = [int(input()) for _ in range(case)] #case만큼 숫자를 입력받아 배열에 저장

#10000까지의 소수를 찾을 필요 없이 입력받은 수 중에 최댓값 까지의 소수를 모두 찾는다

max_num = max(num) #입력받은 숫자들 중 최댓값을 구함
prime_list = [] #소수를 저장하는 리스트
prime_find = [0] * (max_num+1) # 0짜리 배열 생성, 배열의 마지막이 [max_num]이어야 하기 때문에 max_num+1만큼 생성한다
count = 2 #소수를 찾는데 사용할 카운트, 1은 소수가 아니기 때문에 2부터 시작

#max_num 까지의 소수를 모두 찾기
while count <= max_num : #count가 max_num까지 서치
    i = 2   
    while count % i : #count % i의 나머지가 있다? 안으로 들어감, 나머지 없을때까지 i늘려가면서 나눠봄
        i += 1
    if i == count : #i가 자기 자신으로 나눠진다 -> 소수
        prime_list.append(count) #소수 리스트에 저장
        prime_find[count] = 1 #소수 해당하는 부분에 1로 표시해둠
    count += 1

for i in num :
    half = i//2 #가운데 부터 시작
    for j in range(half, 1, -1) : #가운데부터 위,아래로 1씩 나가며 소수 서치
        if prime_find[j] == 1 and prime_find[i - j] == 1 : 
            print(j, i-j)
            break

    