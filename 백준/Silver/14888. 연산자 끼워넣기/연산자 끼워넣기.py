#백트래킹을 이용한 dfs 알고리즘 풀이
import sys
sys.setrecursionlimit(10**7)

max_result = -int(10**9)
min_result = int(10**9)

def dfs(add, sub, mul, div, sum, idx) :
    global max_result, min_result
    if idx == N :
        max_result = max(max_result, sum)
        min_result = min(min_result, sum)
        return
    if add :
        dfs(add-1, sub, mul, div, sum+num[idx], idx + 1)
    if sub :
        dfs(add, sub-1, mul, div, sum-num[idx], idx + 1)
    if mul :
        dfs(add, sub, mul-1, div, sum*num[idx], idx + 1)
    if div :
        dfs(add, sub, mul, div-1, int(sum/num[idx]), idx+1)

N = int(sys.stdin.readline())

num = list(map(int, sys.stdin.readline().split()))

add, sub, mul, div = map(int, sys.stdin.readline().split())

dfs(add, sub, mul, div, num[0], 1)
print(max_result)
print(min_result)