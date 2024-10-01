K,M = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(5)]
alst = list(map(int,input().split()))

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


from collections import deque

def find(arr):
    v = [[False] * 5 for _ in range(5)]
    mx_tmp, mx_tlst = 0, []
    for i in range(5):
        for j in range(5):
            if not v[i][j]:
                tmp, tlst = bfs(i, j, arr, v)
                mx_tmp += tmp
                mx_tlst += tlst

    return mx_tmp, mx_tlst

def bfs(si,sj,arr,v):
    q = deque()
    q.append((si,sj))
    v[si][sj] = True
    tmp = 1
    tlst = []
    tlst.append((si,sj))
    while q:
        ci,cj = q.popleft()
        for ni,nj in ((ci-1,cj),(ci,cj+1),(ci+1,cj),(ci,cj-1)):
            if 0<=ni<5 and 0<=nj<5 and not v[ni][nj] and arr[si][sj] == arr[ni][nj]:
                q.append((ni,nj))
                v[ni][nj] = True
                tmp += 1
                tlst.append((ni,nj))

    if tmp >= 3:
        return tmp, tlst
    else:
        return 0, []

answer = []

for turn in range(1,K+1):
    mx = 0
    mlst = []
    marr = []
    mx90, mx180, mx270 = 0, 0 ,0
    mlst90,mlst180,mlst270 = [],[],[]
    marr90, marr180, marr270 = [], [], []
    ans = 0

    # 1. 탐사 진행
    for sj in range(3):
        for si in range(3):
            tarr90 = rotate90(arr,si,sj)
            tarr180 = rotate180(arr,si,sj)
            tarr270 = rotate270(arr,si,sj)

            mx_tmp90, mx_tlst90 = find(tarr90)
            mx_tmp180, mx_tlst180 = find(tarr180)
            mx_tmp270, mx_tlst270 = find(tarr270)

            if mx_tmp90 > mx90:
                mx90 = mx_tmp90
                mlst90 = mx_tlst90
                marr90 = tarr90

            if mx_tmp180 > mx180:
                mx180 = mx_tmp180
                mlst180 = mx_tlst180
                marr180 = tarr180

            if mx_tmp270 > mx:
                mx270 = mx_tmp270
                mlst270 = mx_tlst270
                marr270 = tarr270

    if mx90 >= max(mx180,mx270):
        mx = mx90
        marr = marr90
        mlst = mlst90

    elif mx180 >= mx270:
        mx = mx180
        marr = marr180
        mlst = mlst180

    else:
        mx = mx270
        marr = marr270
        mlst = mlst270

    if mx == 0:
        break

    ans += mx
    mlst.sort(key=lambda x:(x[1],-x[0]))
    for ti,tj in mlst:
        marr[ti][tj] = alst.pop(0)

    # print('')

    while True:
        mx_tmp, mx_tlst = find(marr)
        if mx_tmp == 0:
            break

        ans += mx_tmp
        mx_tlst.sort(key=lambda x: (x[1], -x[0]))
        for ti, tj in mx_tlst:
            marr[ti][tj] = alst.pop(0)

    # print('')
    arr = marr
    answer.append(ans)
print(*answer)