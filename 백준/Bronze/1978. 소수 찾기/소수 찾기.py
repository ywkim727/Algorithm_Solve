N = int(input())
p_num =list(map(int,input().split())) 

def Prime(x) -> int :   
    count = 0
    for i in x :
        error = 0
        if i > 1 :
            for j in range(2, i) :
                if i % j == 0 :
                    error += 1
            if error == 0 :
                count += 1
    return count    

print(Prime(p_num))

