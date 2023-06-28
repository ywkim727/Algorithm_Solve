def solution(players, callings):
    rank = {i : player for i, player in enumerate(players)}         #등수 : 선수
    player = {player : i for i, player in enumerate(players)}       #선수 : 등수
    #선수:등수(player)에 선수 넣으면 등수
    #등수:선수(rank)에 등수 넣으면 선수
    for i in callings :
        loc = player[i]     #현재 등수
        loc2 = loc-1        #앞 등수
        i2 = rank[loc2]     #앞 선수
        
        rank[loc] = i2
        rank[loc2] = i
        
        player[i2] = loc
        player[i] = loc2
        
    return list(rank.values())