from collections import deque

N = int(input())
K = int(input())

apples = [list(map(int, input().split())) for _ in range(K)]

L = int(input())
command = [input().split() for _ in range(L)]

command_idx = 0
time = 0

snake = deque()

snake.append([1,1])                        #뱀이 1,1에서 부터 시작

dx = [0, 1, 0, -1]                         #방향 인덱스, 시계방향 순서대로 ➡⬇⬅⬆(idx = 0 1 2 3)으로 dx,dy값이 변화
dy = [1, 0, -1, -0]
dir_idx = 0                                #맨 처음 1,1에서 ➡으로 가니까 방향인덱스 0부터 시작

while True :
    time += 1
    x, y = snake[-1]                       #snake배열의 가장 최신의 원소가 현재 위치(머리)가 된다
    x += dx[dir_idx]
    y += dy[dir_idx]
    
    if [x, y] in snake or x < 1 or x > N or y < 1 or y > N : #종료조건 (벽에 닿았을때, 몸에 닿았을때)
        break

    if [x, y] in apples :                  #사과를 먹었을 때는 몸이 늘어나니까 앞으로 간 뒤 꼬리를 제거하지 않음
        snake.append([x, y])
        apples.remove([x, y])              #사과는 먹은 뒤 맵에서 제거
    else :                                 #그냥 앞으로 갈때면 꼬리를 잘라야함(몸의 길이가 늘어나지 않기 때문)
        snake.popleft()
        snake.append([x, y])
    
    if command_idx < L and time == int(command[command_idx][0]) :  
        if command[command_idx][1] == 'D' :
            dir_idx += 1
            dir_idx %= 4                   #dir_idx가 0 1 2 3 에서만 있어야 하기 때문에 4로 나눠준다 (dir_idx = 5 ➡ 1)
        else :
            dir_idx -= 1
            dir_idx %= 4
        command_idx += 1
    
print(time)


