from collections import deque
K, M = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(5)]
tlst = list(map(int,input().split()))
tq = deque()
for t in tlst:
    tq.append(t)
ans = []

def rot90(arr,si,sj):
    narr = [x[:] for x in arr]
    for i in range(3):
        for j in range(3):
            narr[si+i][sj+j] = arr[si+2-j][sj+i]
    return narr

def rot180(arr,si,sj):
    narr = [x[:] for x in arr]
    for i in range(3):
        for j in range(3):
            narr[si+i][sj+j] = arr[si+2-i][sj+2-j]
    return narr

def rot270(arr,si,sj):
    narr = [x[:] for x in arr]
    for i in range(3):
        for j in range(3):
            narr[si+i][sj+j] = arr[si+j][sj+2-i]
    return narr


def simul90(arr): # 90도 회전 함수
    mx = 0
    marr = []
    for sj in range(3):
        for si in range(3):
            arr90 = rot90(arr,si,sj)
            g = []
            v = [[False] * 5 for _ in range(5)]
            tsm = 0
            for i in range(5):
                for j in range(5):
                    if not v[i][j] and (i,j) not in g:
                        g.append(set())
                        cnt = bfs(i,j,g,v,arr90)
                        if cnt >= 3:
                            tsm += cnt
            if tsm > mx:
                mg = []
                mx = tsm
                marr = arr90
                for t in g:
                    if len(t) >= 3:
                        for ti,tj in t:
                            mg.append((ti,tj))
    if mx >= 3:
        return mx, marr, mg
    else:
        return 0, [], []

def simul180(arr): # 90도 회전 함수
    mx = 0
    marr = []
    for sj in range(3):
        for si in range(3):
            arr180 = rot180(arr,si,sj)
            g = []
            v = [[False] * 5 for _ in range(5)]
            tsm = 0
            for i in range(5):
                for j in range(5):
                    if not v[i][j] and (i,j) not in g:
                        g.append(set())
                        cnt = bfs(i,j,g,v,arr180)
                        if cnt >= 3:
                            tsm += cnt
            if tsm > mx:
                mg = []
                mx = tsm
                marr = arr180
                for t in g:
                    if len(t) >= 3:
                        for ti, tj in t:
                            mg.append((ti, tj))
    if mx >= 3:
        return mx, marr, mg
    else:
        return 0, [], []

def simul270(arr): # 90도 회전 함수
    mx = 0
    marr = []
    for sj in range(3):
        for si in range(3):
            arr270 = rot270(arr,si,sj)
            g = []
            v = [[False] * 5 for _ in range(5)]
            tsm = 0
            for i in range(5):
                for j in range(5):
                    if not v[i][j] and (i,j) not in g:
                        g.append(set())
                        cnt = bfs(i,j,g,v,arr270)
                        if cnt >= 3:
                            tsm += cnt
            if tsm > mx:
                mg = []
                mx = tsm
                marr = arr270
                for t in g:
                    if len(t) >= 3:
                        for ti, tj in t:
                            mg.append((ti, tj))
    if mx >= 3:
        return mx, marr, mg
    else:
        return 0, [], []

def bfs(si,sj,g,v,arr):
    q = deque()
    q.append((si,sj))
    v[si][sj] = True
    g[-1].add((si,sj))
    cnt = 1
    while q:
        ci,cj = q.popleft()
        for ni,nj in ((ci-1,cj),(ci,cj+1),(ci+1,cj),(ci,cj-1)):
            if 0<=ni<5 and 0<=nj<5 and not v[ni][nj] and arr[ni][nj] == arr[si][sj]: # 범위 내, 미방문, 같은 숫자
                q.append((ni,nj))
                g[-1].add((ni,nj))
                v[ni][nj] = True
                cnt += 1
    if cnt >= 3:
        return cnt
    else:
        return 0

def simul(arr):
    tsm = 0
    g = []
    v = [[False] * 5 for _ in range(5)]
    for i in range(5):
        for j in range(5):
            if not v[i][j] and (i, j) not in g:
                g.append(set())
                cnt = bfs(i, j, g, v, arr)
                if cnt >= 3:
                    tsm += cnt

    if tsm >= 3:
        mg = []
        for t in g:
            if len(t) >= 3:
                for ti, tj in t:
                    mg.append((ti, tj))
        return tsm,mg
    else:
        return
for turn in range(1,K+1):
    mx = 0
    mg = []
    narr = [x[:] for x in arr]
    # 1. 탐사 진행 (유물 1차 획득 가치 높, 회전 각도 낮, 열 낮, 행 낮)
    a,aarr,ag = simul90(arr)
    b,barr,bg = simul180(arr)
    c,carr,cg = simul270(arr)
    if a == 0 and b == 0 and c == 0: break
    # 90도, 180도, 270도 비교해서 3x3 결정
    if a >= max(b,c):
        mx, arr, mg = a, aarr, ag
    elif b > a and b >= c:
        mx, arr, mg = b, barr, bg
    else:
        mx, arr, mg = c, carr, cg

    while True:
        mg.sort(key=lambda x:(x[1],-x[0])) # 열 낮, 행 높
        for ci,cj in mg:
            arr[ci][cj] = tq.popleft() # 유적 획득 부분을 보조 유적으로 대체
        if not simul(arr): break # 더이상 유물 획득 불가능하면 탈출
        else:
            res, mg = simul(arr)
            mx += res
    ans.append(mx)

for a in ans:
    print(a,end=' ')