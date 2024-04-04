def solution(number, limit, power):
    #약수 구하는 알고리즘 부터
    #약수의 개수가 공격력, 공격력이 limit보다 크면, 공격력 = power
    num = []
    for i in range(1, number+1) :
        count = 0
        for j in range(1, int(i**(1/2))+1) :
            if i%j == 0 :
                count += 1
                if j**2 != i :
                    count += 1
        if count > limit :
            num.append(power)
        else :
            num.append(count)
             
    return sum(num)
        