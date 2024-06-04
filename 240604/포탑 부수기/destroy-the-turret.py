N, M, K = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]
turn = [[0] * M for _ in range(N)]

from collections import deque
def laser(si,sj,ei,ej):
    q = deque()
    q.append((si,sj))
    v = [[[]] * M for _ in range(N)]
    v[si][sj] = [si,sj]
    D = arr[si][sj]
    while q:
        ci,cj = q.popleft()
        if (ci,cj) == (ei,ej):
            arr[ei][ej] = max(0,arr[ei][ej]-D)
            fset.add((ei,ej))
            while True:
                ci,cj = v[ci][cj]
                if (ci,cj) == (si,sj):
                    fset.add((si,sj))
                    return True
                arr[ci][cj] = max(0,arr[ci][cj]-D//2)
                fset.add((ci,cj))
        for di,dj in ((0,1),(1,0),(0,-1),(-1,0)):
            ni,nj = (ci+di)%N,(cj+dj)%M
            if arr[ni][nj] > 0 and not v[ni][nj]:
                q.append((ni,nj))
                v[ni][nj] = [ci,cj]
    return False

def bomb(si,sj,ei,ej):
    fset.add((si,sj))
    fset.add((ei,ej))
    D = arr[si][sj]
    arr[ei][ej] = max(0, arr[ei][ej]-D)
    for di,dj in ((-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1)):
        ni,nj = (ei+di)%N,(ej+dj)%M
        if arr[ni][nj] >0 and (ni,nj) != (si,sj):
            fset.add((ni,nj))
            arr[ni][nj] = max(0, arr[ni][nj]-D//2)



for T in range(1,K+1):
    # 1. 공격자 선정
    mn, mx_turn, si, sj = 5001, 0, 11, 11
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 0: continue # 부서진 포탑 제외
            if arr[i][j] < mn or (arr[i][j]==mn and turn[i][j] > mx_turn) or \
                (arr[i][j] == mn and turn[i][j] == mx_turn and si+sj < i+j) or \
                (arr[i][j] == mn and turn[i][j] == mx_turn and si + sj == i + j and sj < j):
                mn, mx_turn, si, sj = arr[i][j], turn[i][j], i, j

    # 2. 공격 대상 선정
    mx, mn_turn, ei, ej = -1, 1001, 0, 0
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 0: continue  # 부서진 포탑 제외
            if arr[i][j] > mx or (arr[i][j] == mx and turn[i][j] < mn_turn) or \
                (arr[i][j] == mx and turn[i][j] == mn_turn and ei + ej > i + j) or \
                (arr[i][j] == mx and turn[i][j] == mn_turn and ei + ej == i + j and ej > j):
                mx, mn_turn, ei, ej = arr[i][j], turn[i][j], i, j

    arr[si][sj] += (N+M)
    turn[si][sj] = T
    fset = set()
    if not laser(si,sj,ei,ej):
        bomb(si,sj,ei,ej)

    cnt = N*M
    for a in arr:
        cnt -= a.count(0)

    if cnt <= 1: break

    for i in range(N):
        for j in range(M):
            if arr[i][j]>0 and (i,j) not in fset:
                arr[i][j] += 1

print(max(map(max,arr)))