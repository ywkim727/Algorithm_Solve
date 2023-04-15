#분할정복 알고리즘 풀이
#참고 : https://velog.io/@piopiop/%EB%B0%B1%EC%A4%80-6549-%ED%9E%88%EC%8A%A4%ED%86%A0%EA%B7%B8%EB%9E%A8%EC%97%90%EC%84%9C-%EA%B0%80%EC%9E%A5-%ED%81%B0-%EC%A7%81%EC%82%AC%EA%B0%81%ED%98%95%ED%8C%8C%EC%9D%B4%EC%8D%AC
#중간값 m을 기준으로 왼쪽에서 최댓값, 오른쪽에서 최댓값, 두개를 합쳤을때 만들어지는(경계선에 걸치는) 부분의 최댓값 3개를 비교
def histo(l, r):
    if l == r :         #히스토그램을 너비가 1이 될때 까지 반으로 분할, 너비가 1이되면 그 직사각형의 높이를 반환
        return h[l]
    else :              #조각들을 붙이는 과정, 너비가 1이 아니면 return (max(histo(l, m), histo(m+1, r), temp))
        m = (l+r) // 2  #경계선에 걸친 사각형 넓이 temp를 구하는 과정
        nl = m
        nr = m + 1
        nh = min(h[nl], h[nr])  #경계선에 걸친 사각형 의 높이는 h[nr], h[nl]중 작은 높이가 될 것이다
        temp = nh * 2   #경계선에 걸친 직사각형의 넓이 (너비가 2이므로 2를 곱해준다)
        cnt = 2 #너비

        while True :    #nl, nr을 양쪽으로 한칸 씩 늘려가며 생기는 직사각형의 넓이를 구한다
            if (h[nl] == 0 or nl == l) and (h[nr] == 0 or nr == r) :    #nl과 nr이 양쪽 끝에 도착하거나 높이가 0인 사각형을 만나면 종료
                break
            elif h[nl] == 0 or nl == l :    # 한쪽만 끝에 도착했으면 반대쪽만 한칸씩 늘려준다
                if h[nr+1] < nh :           # 매번 nh와 높이를 비교해서 더 작은 쪽을 nh로 업데이트 한다.(직사각형을 만들기 위해, nh보다 높은값을 가져갈 수가 없다)
                    nh = h[nr+1]             
                nr += 1
            elif h[nr] == 0 or nr == r :
                if h[nl-1] < nh :
                    nh = h[nl-1]
                nl -= 1
            else:                           #양쪽 다 늘려갈 수 있을때는 매번 높이를 비교해 작은쪽을 nh에 업데이트한다.
                if h[nl-1] < h[nr+1] :      #넓이의 최대를 구해야 하기 때문에 높이가 더 높은 쪽을 먼저 늘려준다
                    if h[nr+1] < nh :   
                        nh = h[nr + 1]
                    nr += 1
                else :       
                    if h[nl-1] < nh :
                        nh = h[nl - 1]
                    nl -= 1
            cnt += 1                        #한 칸씩 늘려갈 때마다 너비(cnt)를 하나씩 늘려준다
            temp = max(temp, nh*cnt)        #너비를 늘려줄때마다 그때의 넓이(nh*cnt)를 temp와 비교해 temp를 업데이트해 최대를 구한다
        return (max(histo(l, m), histo(m+1, r), temp)) #왼쪽의 최대, 오른쪽의 최대, 경계선 포함의 최대를 비교해 리턴
    
while True:
    h = list(map(int, input().split()))
    if h[0] == 0 :
        break
    print(histo(1, len(h)-1))




