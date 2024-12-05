N, M, F = map(int,input().split())

# 미지의 공간
arr = [list(map(int,input().split())) for _ in range(N)]
# 시간의 벽
cube = [[list(map(int,input().split())) for _ in range(M)] for _ in range(5)]
# 동, 북, 서, 남
cube[1], cube[3], cube[2] = cube[3], cube[2], cube[1]
abnormal = [tuple(map(int,input().split())) for _ in range(F)]
abnormalalive = [1] * F

from collections import deque

def find():
    si, sj = -1, -1
    for i in range(N):
        if sj != -1:
            break
        for j in range(N):
            if arr[i][j] == 3:
                si, sj = i, j
                break

    for i in range(N):
        for j in range(N):
            if arr[i][j] == 3:
                if arr[i][j+1] == 0:
                    cube[0][M-1][M-1-(i-si)] = 3
                    return i, j+1
                elif arr[i-1][j] == 0:
                    cube[1][M-1][M-1-(j-sj)] = 3
                    return i-1, j
                elif arr[i][j-1] == 0:
                    cube[2][M-1][i-si] = 3
                    return i,j-1
                elif arr[i+1][j] == 0:
                    cube[3][M-1][j-sj] = 3
                    return i+1, j

def transform_coords(cd,ni,nj):
    if cd == 4:  # 윗면에서 다른 면으로 넘어가는 경우
        if ni < 0:
            return 1,0,M-1-nj
        elif ni >=M:
            return 3,0,nj
        elif nj < 0:
            return 2,0,ni
        elif nj >=M:
            return 0,0,M-1-ni

    elif cd ==0: # 동쪽에서 다른 면으로
        if ni < 0:
            return 4, M-1-nj, M-1
        elif ni >= M:
            return False
        elif nj < 0:
            return 3,ni, M-1
        elif nj >= M:
            return 1, ni, 0

    elif cd ==1: # 북쪽에서 다른 면으로
        if ni < 0:
            return 4, 0, M-1-nj
            # return 4,nj,0
        elif ni >= M:
            return False
        elif nj < 0:
            return 0,ni,M-1
        elif nj >= M:
            return 2,ni,0

    elif cd ==2: # 서쪽에서 다른 면으로
        if ni < 0:
            return 4, nj, 0
            # return 4,0,M-1-nj
        elif ni >= M:
            return False
        elif nj < 0:
            return 1,ni,M-1
        elif nj >= M:
            return 3,ni,0

    elif cd ==3: # 남쪽에서 다른 면으로
        if ni < 0:
            return 4, M-1, nj
        elif ni >= M:
            return False
        elif nj < 0:
            return 2,ni,M-1
        elif nj >= M:
            return 0,ni,0

def bfs1():
    # 1. 맨 윗단에서 우주선 찾기
    si,sj = -1, -1
    for i in range(M):
        if sj != -1:
            break
        for j in range(M):
            if cube[4][i][j] == 2:
                si,sj = i,j
                break
    # 2. bfs 시작
    v = [[[0] * M for _ in range(M)] for _ in range(5)]
    v[4][si][sj] = 1
    q = deque()
    q.append((4,si,sj,0))
    while q:
        cd, ci, cj, cnt = q.popleft()

        if cube[cd][ci][cj] == 3:
            return cnt

        for ni,nj in ((ci-1,cj),(ci,cj+1),(ci+1,cj),(ci,cj-1)):
            if not (0<=ni<M and 0<=nj<M):
                result = transform_coords(cd,ni,nj)
                if not result:
                    continue
                else:
                    dir,ni,nj = result
            else:
                dir = cd

            if not v[dir][ni][nj] and cube[dir][ni][nj] != 1:
                v[dir][ni][nj] = 1
                q.append((dir,ni,nj,cnt+1))

    return -1

def bfs2(cnt,si,sj):
    abnormalarr = [[-1] * N for _ in range(N)]
    dlst = [(0,1),(0,-1),(1,0),(-1,0)]

    for i in range(F):
        ci,cj,cd,cv = abnormal[i]
        abnormalarr[ci][cj] = 0
        time = cv

        while True:
            di,dj = dlst[cd]
            ni,nj = ci+di,cj+dj
            if not (0<=ni<N and 0<=nj<N):
                break
            if arr[ni][nj] == 1 or arr[ni][nj] == 4:
                break
            abnormalarr[ni][nj] = time
            time += cv
            ci,cj = ni,nj
    v = [[0] * N for _ in range(N)]
    v[si][sj] = 1
    q = deque()
    q.append((si,sj,cnt+1))

    while q:
        ci,cj,cnt = q.popleft()
        if arr[ci][cj] == 4:
            return cnt

        for di,dj in dlst:
            ni,nj = ci+di, cj+dj
            if not (0<=ni<N and 0<=nj<N):
                continue
            if not v[ni][nj] and (arr[ni][nj] == 0 or arr[ni][nj]==4) and \
                    (abnormalarr[ni][nj] == -1 or (-1<cnt+1<abnormalarr[ni][nj])):
                v[ni][nj] = 1
                q.append((ni,nj,cnt+1))
    return -1


# 1. 시간의 벽에 탈출구 기록, 바닥 탈출구 받기
si,sj = find()
# 2. 시간의 벽에서 3차원 BFS 진행
cnt = bfs1()
# print(cnt)
# 3. 미지공간에서 이상현상 고려하여 2차원 BFS 진행
ans = bfs2(cnt,si,sj)

print(ans)