from collections import deque

K, M = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(5)]
tlst = list(map(int,input().split())) # 대비 조각들
tq = deque()
for t in range(len(tlst)):
    tq.append(tlst[t])

def rotate90(arr,si,sj):
    narr = [x[:] for x in arr]
    for i in range(3):
        for j in range(3):
            narr[si+i][sj+j] = arr[si+2-j][sj+i]
    return narr

def rotate180(arr,si,sj):
    narr = [x[:] for x in arr]
    for i in range(3):
        for j in range(3):
            narr[si+i][sj+j] = arr[si+2-i][sj+2-j]
    return narr

def rotate270(arr,si,sj):
    narr = [x[:] for x in arr]
    for i in range(3):
        for j in range(3):
            narr[si+i][sj+j] = arr[si+j][sj+2-i]
    return narr

# 유적 탐사
def bfs(si,sj,arr,v,group):
    q = deque()
    q.append((si,sj))
    v[si][sj] = True
    group[-1].add((si,sj))
    cnt = 1
    while q:
        ci,cj = q.popleft()
        for ni,nj in ((ci-1,cj),(ci+1,cj),(ci,cj-1),(ci,cj+1)):
            if 0<=ni<5 and 0<=nj<5 and not v[ni][nj] and arr[si][sj] == arr[ni][nj]: # 범위내, 미방문, 같은 숫자
                q.append((ni,nj))
                group[-1].add((ni,nj))
                v[ni][nj] = True
                cnt += 1
    if cnt >=3:
        return cnt
    else:
        return 0

def simulation90(arr,mx):
    marr1 = []
    ag = []
    # 1. 탐사 진행 함수
    for i in range(3):
        for j in range(3):
            arr1 = rotate90(arr, j, i)  # 90도 회전
            asm = 0
            v1 = [[False] * 5 for _ in range(5)]
            g1 = []
            for ci in range(5):
                for cj in range(5):
                    if not v1[ci][cj] and (ci, cj) not in g1:
                        g1.append(set())
                        tmp = bfs(ci, cj, arr1, v1, g1)
                        if tmp >= 3:
                            asm += tmp
            if asm > mx:
                mx = asm
                marr1 = arr1
                ag = []
                for g in g1:
                    if len(g) >= 3:
                        for ci, cj in g:
                            ag.append((ci, cj))

    return marr1,mx,ag

def simulation180(arr,mx):
    marr1 = []
    ag = []
    # 1. 탐사 진행 함수
    for i in range(3):
        for j in range(3):
            arr1 = rotate180(arr, j, i)  # 180도 회전
            asm = 0
            v1 = [[False] * 5 for _ in range(5)]
            g1 = []
            for ci in range(5):
                for cj in range(5):
                    if not v1[ci][cj] and (ci, cj) not in g1:
                        g1.append(set())
                        tmp = bfs(ci, cj, arr1, v1, g1)
                        if tmp >= 3:
                            asm += tmp
            if mx < asm:
                mx = asm
                marr1 = arr1
                ag = []
                for g in g1:
                    if len(g) >= 3:
                        for ci, cj in g:
                            ag.append((ci, cj))


    return marr1,mx,ag

def simulation270(arr,mx):
    marr1 = []
    ag = []
    # 1. 탐사 진행 함수
    for i in range(3):
        for j in range(3):
            arr1 = rotate270(arr, j, i)  # 270도 회전
            asm = 0
            v1 = [[False] * 5 for _ in range(5)]
            g1 = []
            for ci in range(5):
                for cj in range(5):
                    if not v1[ci][cj] and (ci, cj) not in g1:
                        g1.append(set())
                        tmp = bfs(ci, cj, arr1, v1, g1)
                        if tmp >= 3:
                            asm += tmp
            if mx < asm:
                mx = asm
                marr1 = arr1
                ag = []
                for g in g1:
                    if len(g) >= 3:
                        for ci, cj in g:
                            ag.append((ci, cj))


    return marr1,mx,ag

def sim(arr):
    mx = 0
    sm = 0
    v = [[False] * 5 for _ in range(5)]
    g1 = []
    for ci in range(5):
        for cj in range(5):
            if not v[ci][cj] and (ci, cj) not in g1:
                g1.append(set())
                tmp = bfs(ci, cj, arr, v, g1)
                if tmp >= 3:
                    sm += tmp
    if sm > 0:
        mx = sm
        ag = []
        for g in g1:
            if len(g) >= 3:
                for ci, cj in g:
                    ag.append((ci, cj))
        return mx,ag
    else:
        return
ans = []
# 탐사는 K턴동안 진행
for _ in range(K):
    # 회전목표 : 유물 1차 획득까지 최대화, 회전각 작은, 열 작고, 행 작고

    # 1.1 탐사 진행 3x3 격자 획득하는 부분
    mx = 0
    aarr = [x[:] for x in arr]
    arr1, a, ag = simulation90(arr,0)
    arr2, b, bg = simulation180(arr,0)
    arr3, c, cg = simulation270(arr,0)

    if a < 3 and b < 3 and c < 3 : break
    # if a == 0 : break
    # arr = arr1
    # tg = ag
    # mx = a

    if a >= max(b,c): # a가 가장 큼
        arr = arr1
        tg = ag
        mx = a
    elif b > c : # b 가 가장 큼
        arr = arr2
        tg = bg
        mx = b
    else: # c가 가장 큼
        arr = arr3
        tg = cg
        mx = c


    # 연쇄 획득 부분
    while True:
        tg.sort(key=lambda x: (x[1], -x[0]))
        for ci, cj in tg:
            arr[ci][cj] = tq.popleft()
        if sim(arr) is None: break

        t, tg = sim(arr)
        mx += t

    ans.append(mx)

for i in range(len(ans)):
    print(ans[i], end=' ')