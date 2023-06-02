n, m = map(int, input().split())

graph = []

for _ in range(n) :
    graph.append(input())

result = []

for i in range(n-7):                            #n,m에 -7을 해주는 이유는 이 지점부터 8X8크기를 검사할 것이기 때문에 전체 보드판의 인덱스를 벗어나지 않기 위함
    for j in range(m-7):
        w_draw = 0                              #w_draw : W로 시작할 경우, b_draw : B로 시작할 경우
        b_draw = 0
        for a in range(i, i+8):                 
            for b in range(j, j+8):
                if (a+b) % 2 == 0 :             #a+b가 짝수라면 시작한 칸과 같아야하고 홀수면 달라야 함
                    if graph[a][b] == 'W' :
                        w_draw += 1
                    elif graph[a][b] == 'B' :
                        b_draw += 1
                else :
                    if graph[a][b] == 'W' :
                        b_draw += 1
                    elif graph[a][b] == 'B' :
                        w_draw += 1
        result.append(min(w_draw, b_draw))

print(min(result))   