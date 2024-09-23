K, M = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(5)]
left = list(map(int,input().split()))


from collections import deque
anlst = []

def bfs(arr,si,sj,v):
    q = deque()
    q.append((si,sj))
    v[si][sj] = True
    tmp = 1
    tlst = [(si,sj)]
    while q:
        ci,cj = q.popleft()
        for ni,nj in ((ci-1,cj),(ci,cj+1),(ci+1,cj),(ci,cj-1)):
            if 0<=ni<5 and 0<=nj<5 and not v[ni][nj] and arr[si][sj] == arr[ni][nj]:
                q.append((ni,nj))
                v[ni][nj] = True
                tmp += 1
                tlst.append((ni,nj))

    return tmp,tlst

def find(arr):
    v = [[False] * 5 for _ in range(5)]
    tmp, tlst = 0, []
    for i in range(5):
        for j in range(5):
            if not v[i][j]:
                cnt,clst = bfs(arr,i,j,v)
                if cnt < 3: continue
                tmp += cnt
                tlst += clst
    return tmp, tlst

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


for turn in range(K):
    ans = 0
    mx,mlst,marr = 0, [], []
    mx90, mx180, mx270 = 0, 0, 0
    # 1. 탐사 진행
    # 1.1 3x3 격자 선택
    for j in range(3):
        for i in range(3):
            arr90 = rot90(arr,i,j)
            arr180 = rot180(arr,i,j)
            arr270 = rot270(arr,i,j)

            a,alst = find(arr90)
            b,blst = find(arr180)
            c,clst = find(arr270)


            # 1.2.1 90도가 가장 클 떄
            if a > mx90:
                mx90 = a
                mlst90 = alst
                marr90 = arr90
            # 1.2.2 180도가 가장 클 때
            if b > mx180:
                mx180 = b
                mlst180 = blst
                marr180 = arr180
            # 1.2.3 270도가 가장 클 때
            if c > mx270:
                mx270 = c
                mlst270 = clst
                marr270 = arr270
    #         print('')
    # print('')

    if mx90 == 0 and mx180 == 0 and mx270 == 0: break

    if mx90 >= max(mx180,mx270):
        mx = mx90
        mlst = mlst90
        marr = marr90
    elif mx180 >= mx270:
        mx = mx180
        mlst = mlst180
        marr = marr180
    else:
        mx = mx270
        mlst = mlst270
        marr = marr270

    # print('')
    ans += mx


    mlst.sort(key=lambda x:(x[1],-x[0]))
    for ti, tj in mlst:
        marr[ti][tj] = left.pop(0)
    # print('')


    while True:
        tmp, tlst = find(marr)
        if tmp < 3: break
        ans += tmp

        tlst.sort(key=lambda x: (x[1], -x[0]))
        for ti, tj in tlst:
            marr[ti][tj] = left.pop(0)
    arr = marr
    anlst.append(ans)
print(*anlst)