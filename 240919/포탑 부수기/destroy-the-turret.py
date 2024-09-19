N, M, K = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]
turn = [[0] * M for _ in range(N)]

from collections import deque
def laser(si,sj,ei,ej):
    q = deque()
    q.append((si,sj))
    v = [[[] for _ in range(M)] for _ in range(N)]
    v[si][sj] = [si,sj]
    D = arr[si][sj]
    while q:
        ci,cj = q.popleft()
        if (ci,cj) == (ei,ej):
            arr[ci][cj] = max(0, arr[ci][cj] - D)
            while True:
                ci,cj = v[ci][cj]
                if (ci,cj) == (si,sj):
                    return True
                fset.add((ci,cj))
                arr[ci][cj] = max(0,arr[ci][cj]-D//2)

        for di,dj in ((0,1),(1,0),(0,-1),(-1,0)):
            ni,nj = (ci+di)%N, (cj+dj)%M
            if arr[ni][nj] > 0 and not v[ni][nj]:
                q.append((ni,nj))
                v[ni][nj] = [ci,cj]
    return False

def bomb(si,sj,ei,ej):
    D = arr[si][sj]
    arr[ei][ej] = max(0,arr[ei][ej]-D)
    for di,dj in ((-1,-1),(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1)):
        ni, nj = (ei + di) % N, (ej + dj) % M
        if (ni,nj) != (si,sj) and arr[ni][nj] > 0:
            arr[ni][nj] = max(0, arr[ni][nj] - D // 2)
            fset.add((ni,nj))

for T in range(1,K+1):
    # 1. 공격자 선정
    mn,mn_turn,si,sj = 5001,0, N, M
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 0: continue
            # 공격력이 가장 낮은, 가장 최근에 공격한, 행과 열의 합이 가장 큰, 열 값이 가장 큰
            if arr[i][j] < mn or (arr[i][j]==mn and mn_turn < turn[i][j]) or \
                (arr[i][j] == mn and mn_turn == turn[i][j] and si+sj < i+j ) or \
                (arr[i][j] == mn and mn_turn == turn[i][j] and si + sj == i + j and sj < j):
                mn,mn_turn,si,sj = arr[i][j], turn[i][j], i, j

    # 2. 공격 대상 선정
    mx,mx_turn,ei,ej = 0,1001, N, M
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 0: continue
            # 공격력이 가장 높은, 가장 공격한게 오래된, 행과 열의 합이 가장 작은, 열 값이 가장 작은
            if arr[i][j] > mx or (arr[i][j]==mx and mx_turn > turn[i][j]) or \
                (arr[i][j] == mx and mx_turn == turn[i][j] and ei+ej > i+j ) or \
                (arr[i][j] == mx and mx_turn == turn[i][j] and ei + ej == i + j and ej > j):
                mx,mx_turn,ei,ej = arr[i][j], turn[i][j], i, j

    # 3. 공격자 업데이트
    arr[si][sj] += (N+M)
    turn[si][sj] = T
    fset = set()
    fset.add((si,sj))
    fset.add((ei,ej))

    if not laser(si,sj,ei,ej):
        bomb(si,sj,ei,ej)

    # 종료조건
    cnt = N*M
    for lst in arr:
        cnt -= lst.count(0)
    if cnt <= 1: break

    # 4. 포탑 정비
    for i in range(N):
        for j in range(M):
            if arr[i][j] > 0 and (i,j) not in fset:
                arr[i][j] += 1


print(max(map(max,arr)))