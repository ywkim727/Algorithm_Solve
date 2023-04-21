import sys
sys. setrecursionlimit(10**9)                       #재귀의 깊이를 설정해 줍니다

tree = []
while True :
    try :
        tree.append(int(sys.stdin.readline()))      #입력이 없을때 까지 tree에 append
    except :
        break

def postorder(start, end) :                         #루트 노드를 기준으로 루트보다 큰원소(왼쪽 서브트리)와 작은원소(오른쪽 서브트리)로 나눈다    
    if start > end :
        return
    mid = end + 1                                   #mid를 end+1로 초기화 하는 이유 : 원소들이 전부 루트노드보다 작은 경우
    for i in range(start+1, end+1) :                #첫번째(왼쪽서브트리) postorder는 (start+1, end), 두번째(오른쪽 서브트리)는 (end+1, end)이므로
        if tree[i] > tree[start] :                  #if start > end에 의해 return된다 
            mid = i                                 #루트보다 큰 원소가 나오는 지점을 찾아서 mid로 업데이트, 이후 mid 기준으로 왼쪽,오른쪽 서브트리 나눈다
            break
    postorder(start+1, mid-1)                       #왼쪽 트리
    postorder(mid, end)                             #오른쪽 트리
    print(tree[start])                              #루트 노드

postorder(0, len(tree)-1)