N, M, K = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]
turn = [[0] * M for _ in range(N)]

from collections import deque

# [4] 레이저 공격
def laser(si,sj,ei,ej):
    q = deque()
    q.append((si,sj))
    v = [[[] for _ in range(M)] for _ in range(N)]
    v[si][sj] = (si,sj)
    d = arr[si][sj]

    while q:
        ci,cj = q.popleft()
        if (ci,cj) == (ei,ej): # 공격대상 도착
            arr[ei][ej] = max(0,arr[ei][ej]-d)
            while True:
                ci,cj = v[ci][cj]
                if (ci,cj) == (si,sj):
                    return True
                arr[ci][cj] = max(0,arr[ci][cj] - d//2)
                fset.add((ci,cj))

        for di,dj in ((0,1),(1,0),(0,-1),(-1,0)):
            ni,nj = (ci+di)%N, (cj+dj)%M
            if arr[ni][nj]>0 and not v[ni][nj]:
                q.append((ni,nj))
                v[ni][nj] = (ci,cj)

    return False

# [5] 포탄 공격
def bomb(si,sj,ei,ej):
    d = arr[si][sj]
    arr[ei][ej] = max(0,arr[ei][ej]-d)

    for di,dj in ((0,-1),(-1,-1),(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1)):
        ni,nj = (ei+di)%N, (ej+dj)%M
        if (ni,nj) != (si,sj):
            arr[ni][nj] = max(0,arr[ni][nj]-d//2)
            fset.add((ni,nj))

# K턴 동안 반복
for T in range(1,K+1):

    # [1] 공격자 선정
    mn, mx_turn, si, sj = 5001, 0, -1, -1
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 0 : continue
            # [1-1] 공격력 낮고, 최근 턴에 공격했고, 행+열 큰, 열 큰
            if arr[i][j] < mn or (arr[i][j]==mn and mx_turn < turn[i][j]) or \
                (arr[i][j]==mn and turn[i][j] == mx_turn and si+sj < i+j) or \
                (arr[i][j]==mn and turn[i][j] == mx_turn and si+sj==i+j and sj<j):
                mn, mx_turn, si, sj = arr[i][j], turn[i][j], i, j

    # [2] 공격대상 선정
    mx, mn_turn, ei, ej = -1, 1001,11,11
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 0 : continue
            # [2-1] 공격력 높고, 공격한지 가장 오래되었고, 행+열 작고, 열 작은
            if arr[i][j] > mx or (arr[i][j]==mx and mn_turn > turn[i][j]) or \
                (arr[i][j] == mx and mn_turn == turn[i][j] and ei+ej > i+j) or \
                (arr[i][j] == mx and mn_turn == turn[i][j] and ei+ej == i+j and ej>j):
                mx, mn_turn, ei, ej = arr[i][j], turn[i][j], i, j

    # [3] 공격자 공격력 상승 및 fset에 경로 추가
    arr[si][sj] += (M+N) # 공격자 공격력 상승
    turn[si][sj] = T # 턴 기록
    fset = set()
    # 공격자, 대상 경로 추가
    fset.add((si,sj))
    fset.add((ei,ej))

    if laser(si,sj,ei,ej) == False:
        bomb(si,sj,ei,ej)

    cnt = N*M
    for lst in arr:
        cnt -= lst.count(0)
    if cnt <=1 :
        break

    # [6] 포탑 정비
    for i in range(N):
        for j in range(M):
            if (arr[i][j] > 0 and (i,j) not in fset):
                arr[i][j] += 1

print(max(map(max,arr)))