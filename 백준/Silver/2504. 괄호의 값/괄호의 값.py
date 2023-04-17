bracket = list(input())

stack = []

temp = 1
answer = 0

for i in range(len(bracket)) :
    if bracket[i] == '(' :
        stack.append(bracket[i])                #스택에 ( 추가하고 temp *2
        temp *= 2

    elif bracket[i] == '[' :
        stack.append(bracket[i])                #스택에 [ 추가하고 temp *2
        temp *= 3

    elif bracket[i] == ')' :
        if not stack or stack[-1] == '[' :      #스택이 비었거나 짝이 안맞을때
            answer = 0
            break
        if bracket[i-1] == '(' :                #직전에 (가 있었으면 (직전에 있는 괄호의 문을 닫았으면)
            answer += temp
        stack.pop()                             #스택에서 직전에 있었던 ( 제거 (문을 닫았으니까) 
        temp //= 2                              #괄호 문을 열면서 이미 곱해주었기 때문에 닫으면서 다시 원상복구 한다

    elif bracket[i] == ']' :
        if not stack or stack[-1] == '(' :
            answer = 0
            break
        if bracket[i-1] == '[' :
            answer += temp
        stack.pop()
        temp //= 3

if stack :
    print(0)
else :
    print(answer)

# 한 가지 주의해야 할 점은 꺼낸 괄호가 닫는 괄호일 때,

# 괄호 입력 배열에서의 그 괄호의 바로 직전의 괄호가 쌍이 맞는 경우에만 곱하기를 한다.

# ( stack이 아닌 bracket 배열의 인덱스 )

 
# 즉, ' [ ( ) ] ' 처럼 마지막 ' ] ' 의 바로 직전의 괄호가 ' [ ' 가 아닌 ' ) ' 이기 때문에

# 값을 더해가지 않는다.

 
# 여기서 우리가 계산해야 할 것은 3 x 2 = 6인데

# 앞에서 곱하기 3은 이미 계산을 했기 때문에 뒤에서 더 계산을 하면 안되기 때문이다.