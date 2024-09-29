N, M = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]

from collections import deque
def bfs(si,sj):
    q = deque()
    q.append((si,sj))
    v = [[False] * N for _ in range(N)]
    v[si][sj] = True
    rlst, clst = [], [(si,sj)]
    while q:
        ci,cj = q.popleft()
        for ni,nj in ((ci-1,cj),(ci,cj+1),(ci+1,cj),(ci,cj-1)):
            if 0<=ni<N and 0<=nj<N and not v[ni][nj]:
                if arr[ni][nj] > 0 and arr[si][sj] == arr[ni][nj]:
                    q.append((ni,nj))
                    v[ni][nj] = True
                    clst.append((ni,nj))
                elif arr[ni][nj] == 0:
                    q.append((ni,nj))
                    v[ni][nj] = True
                    rlst.append((ni,nj))

    if len(rlst)+len(clst) >= 2:
        return rlst,clst
    else:
        return [],[]

def gravity(arr):
    for j in range(N):
        for i in range(N-1,-1,-1):
            if arr[i][j] >= 0:
                ci = i
                while True:
                    ci += 1
                    if 0<=ci<N and arr[ci][j]==-2:
                        arr[ci][j] = arr[ci-1][j]
                        arr[ci-1][j] = -2
                    else:
                        break
    return arr

ans = 0

while True:

    # 1. 폭탄 묶음 찾기
    mx = 0
    rlst,clst = [], []
    for i in range(N-1,-1,-1):
        for j in range(N):
            if arr[i][j] > 0:
                trlst,tclst = bfs(i,j)
                if not trlst and not tclst: continue

                if len(trlst) + len(tclst) > mx:
                    mx = len(trlst) + len(tclst)
                    rlst, clst = trlst, tclst
                elif len(trlst) + len(tclst) == mx:
                    if len(trlst) < len(rlst):
                        rlst, clst = trlst, tclst
    # 2. 폭탄 제거
    tlst = rlst + clst
    if len(tlst) < 2 : break
    else:
        ans += len(tlst) ** 2
    # narr = [x[:] for x in arr]
    for ti,tj in tlst:
        arr[ti][tj] = -2
    # print('')

    # # (디버깅용)
    # # 3. 중력
    # narr1 = [x[:] for x in arr]
    # arr1 = gravity(arr)
    # print('')
    #
    # # 4. 90도 반시계(270도)
    # narr2 = [x[:] for x in arr1]
    # arr2 = list(map(list,zip(*arr1)))[::-1]
    # print('')
    #
    # # 5. 중력
    # narr3 = [x[:] for x in arr2]
    # arr = gravity(arr2)
    # print('')

    # 3. 중력
    # print('')
    arr = gravity(arr)
    # print('')
    # 4. 90도 반시계(270도)
    arr = list(map(list,zip(*arr)))[::-1]
    # print('')
    # 5. 중력
    arr = gravity(arr)
    # print('')
print(ans)