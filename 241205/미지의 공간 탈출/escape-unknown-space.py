N, M, F = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]
# 동, 북, 서, 남, 윗면
cube = [[list(map(int,input().split())) for _ in range(M)] for _ in range(5)]
cube[1],cube[2],cube[3] = cube[3],cube[1],cube[2]
# [1] 타임머신 시작점 찾기
flst = [list(map(int,input().split())) for _ in range(F)]
def find_tm():
    si,sj = N,N
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 3:
                si,sj = i,j
                break
        if sj != N:
            break

    # dr = 5
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 3:
                if arr[i-1][j] == 0:
                    # dr = 1
                    cube[1][M-1][M-1-(j-sj)] = 3
                    return i-1,j
                elif arr[i][j+1] == 0:
                    # dr = 0
                    cube[0][M-1][M-1-(i-si)] = 3
                    return i,j+1
                elif arr[i+1][j] == 0:
                    # dr = 3
                    cube[3][M-1][j-sj] = 3
                    return i+1,j
                elif arr[i][j-1] == 0:
                    # dr = 2
                    cube[2][M-1][i-si] = 3
                    return i,j-1

def trans_coord(ci,cj,cd):
    if cd == 4: # 윗면
        if ci<0: # 북
            return 0, M-1-cj, 1
        elif ci >= M: # 남
            return 0, cj, 3
        elif cj <0:
            return 0, ci, 2
        elif cj >=M:
            return 0,M-1-ci, 0

    elif cd == 0: # 동쪽
        # if ci < 0:
        #     return
        if cj < 0:
            return ci,M-1,3
        elif cj >=M:
            return ci,0,1
        elif ci < 0:
            return cj,M-1,4

    elif cd == 1: # 북쪽
        if cj < 0:
            return ci,M-1,0
        elif cj >= M:
            return ci,0,2
        elif ci < 0:
            return 0,M-1-cj,4

    elif cd == 2: # 서쪽
        if cj < 0:
            return ci,M-1,1
        elif cj >= M:
            return ci,0,3
        elif ci < 0:
            return cj,0,4

    elif cd == 3: # 남쪽
        if cj < 0:
            return ci,M-1,2
        elif cj >= M:
            return ci,0,0
        elif ci < 0:
            return M-1,cj,4
    else:
        return


from collections import deque
def find_tw():
    si,sj = N,N
    for i in range(M):
        for j in range(M):
            if cube[4][i][j] == 2:
                si,sj = i, j
    q = deque()
    q.append((si,sj,4,0)) # ci, cj, cd, cnt
    v = [[[0] * M for _ in range(M)] for _ in range(5)]
    v[4][si][sj] = True
    while q:
        ci,cj,cd,cnt = q.popleft()

        if cube[cd][ci][cj] == 3:
            return cnt

        for ni,nj in ((ci-1,cj),(ci,cj+1),(ci+1,cj),(ci,cj-1)):
            dir = cd
            if not (0<=ni<M and 0<=nj<M):
                result = trans_coord(ni, nj, dir)
                if result is None:
                    continue
                else:
                    ni, nj, dir = result
            if not v[dir][ni][nj] and cube[dir][ni][nj] != 1:
                q.append((ni,nj,dir,cnt+1))
                v[dir][ni][nj] = True

di,dj = [0,0,1,-1], [1,-1,0,0]

def find_exit(si,sj,cnt,flst):
    q = deque()
    q.append((si,sj,cnt))
    v = [[False] * N for _ in range(N)]
    v[si][sj] = True

    fv = [[0] * N for _ in range(N)]
    for i in range(len(flst)):
        ci,cj,cd,cv = flst[i]
        fv[ci][cj] = 1
        while True:
            ci,cj = ci+di[cd], cj+dj[cd]
            if not (0<=ci<N and 0<=cj<N) or arr[ci][cj] != 0:
                break
            fv[ci][cj] = cv
            cv += cv
    # print('')
    while q:
        ci,cj,cnt = q.popleft()
        if arr[ci][cj] == 4:
            return cnt
        for ni,nj in ((ci-1,cj),(ci+1,cj),(ci,cj-1),(ci,cj+1)):
            if 0<=ni<N and 0<=nj<N and arr[ni][nj] != 1 and not v[ni][nj] and (not fv[ni][nj] or cnt+1<fv[ni][nj]):
                q.append((ni,nj,cnt+1))
                v[ni][nj] = True

    return -1
si,sj = find_tm()
cnt = find_tw()
ans = find_exit(si,sj,cnt+1,flst)
print(ans)