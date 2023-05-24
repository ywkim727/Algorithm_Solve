N = int(input())

num = []
ans = []
cur = 1
flag = 0

for i in range(N) :
    target = int(input())
    while cur <= target :       #입력한 수를 만날때까지 push
        num.append(cur)
        ans.append('+')
        cur += 1
    if num[-1] == target :      #stack의 꼭대기가 입력한 숫자와 같으면 pop
        num.pop()
        ans.append('-')
    else :                      #stack의 꼭대기가 입력한 숫자와 같지 않으면 주어진 수열을 만들 수 없음
        print("NO")             #오름차순으로 스택이 입력되는데 꼭대기가 target보다 크면 target은 꼭대기보다 아래에 쌓여있어 pop할 수 없음
        flag = 1
        break

if flag == 0 :
    for i in ans :
        print(i)