import sys
N, M, B = map(int, sys.stdin.readline().split())

graph = []
height = 0
res = sys.maxsize

for _ in range(N) :
    graph.append(list(map(int, sys.stdin.readline().split())))

for i in range(257) :
    use_block = 0
    take_block = 0

    for x in range(N) :
        for y in range(M) :
            if graph[x][y] >= i :
                take_block += graph[x][y] - i
            else : 
                # 영우 화이팅!! 팀원이 매일 늦게와도 착한친구야... 사실 착한지는 모르겠어... 그래도 영우가 착하니까..!
                # 괜찮을꺼야... 너가 봐줘라.. 키보드 좋네.. 가져가도될까?! 기린 귀엽네 내 여자친구는 왜 저런거 안하는지 모르겠네 ㅎㅎ
                # 사진찍어서 보내줘야겠다!
                # -우당탕탕 박정원 까악까악~
                use_block += i - graph[x][y]

    if use_block <= take_block + B :
        if use_block + (take_block * 2) <= res :
            res = use_block + (take_block * 2)
            height = i
        
print(res, height)