K, M = map(int,input().split())
# 5x5 arr
arr = [list(map(int,input().split())) for _ in range(5)]


# 유물 벽면
from collections import deque
tq = deque(list(map(int,input().split())))
alst = []

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

def simul(arr):
    v = [[False] * 5 for _ in range(5)]
    cnt = 0

    for i in range(5):
        for j in range(5):
            if not v[i][j] and arr[i][j] > 0:
                v[i][j] = True
                arr, tmp = bfs(arr,i,j,v)
                if tmp < 3: continue
                cnt += tmp
    return arr, cnt

def bfs(arr,si,sj,v):
    q = deque()
    q.append((si,sj))
    fset = set()
    cnt = 1
    while q:
        ci,cj = q.popleft()
        for ni, nj in ((ci-1,cj),(ci,cj+1),(ci+1,cj),(ci,cj-1)):
            if 0<=ni<5 and 0<=nj<5 and not v[ni][nj] and arr[si][sj] == arr[ni][nj]:
                q.append((ni,nj))
                v[ni][nj] = True
                fset.add((ni,nj))
                cnt += 1

    if cnt >= 3:
        arr[si][sj] = 0
        for ti,tj in fset:
            arr[ti][tj] = 0
    return arr, cnt

# K턴 동안 진행
for turn in range(1,K+1):
    ans = 0
    # 1. 탐사 진행
    # 회전 목표 (유물 1차 높, 회전 각도 낮, 열 낮, 행 낮)
    amx, aarr = 0, []
    bmx, barr = 0, []
    cmx, carr = 0, []
    for j in range(3):
        for i in range(3):
            # 1-a 회전
            taarr = rot90(arr,i,j)
            tbarr = rot180(arr,i,j)
            tcarr = rot270(arr,i,j)
            # print('')
            # 1-b 유물 획득
            taarr,ta = simul(taarr)
            if amx < ta:
                amx = ta
                aarr = taarr
            tbarr,tb = simul(tbarr)
            if bmx < tb:
                bmx = tb
                barr = tbarr
            tcarr,tc = simul(tcarr)
            if cmx < tc:
                cmx = tc
                carr = tcarr

    # 종료 조건
    if amx == 0 and bmx == 0 and cmx == 0: break


    mx, marr = 0, []

    # 2. 유물 채우기
    # 90도가 가장 큼
    if amx >= max(bmx,cmx):
        mx, marr = amx, aarr
    # 180도가 가장 큼
    elif bmx >= cmx:
        mx, marr = bmx, barr
    # 270도가 가장 큼
    else:
        mx, marr = cmx, carr

    ans += mx

    for j in range(5):
        for i in range(4,-1,-1):
            if marr[i][j] == 0:
                marr[i][j] = tq.popleft()

    while True:
        marr,cnt = simul(marr)
        if cnt < 3: break
        ans += cnt
        for j in range(5):
            for i in range(4, -1, -1):
                if marr[i][j] == 0:
                    marr[i][j] = tq.popleft()
    arr = marr
    alst.append(ans)
print(*alst)