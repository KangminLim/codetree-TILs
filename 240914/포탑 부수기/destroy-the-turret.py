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
            arr[ei][ej] = max(0,arr[ei][ej] - D)
            fset.add((ei,ej))
            while True:
                ci,cj = v[ci][cj]
                fset.add((ci,cj))
                if (ci,cj) == (si,sj):
                    return True
                arr[ci][cj] = max(0, arr[ci][cj] - D//2)


        for di,dj in ((0,1),(1,0),(0,-1),(1,0)):
            ni,nj = (ci+di)%N, (cj+dj)%M
            if not v[ni][nj] and arr[ni][nj] >= 1:
                q.append((ni,nj))
                v[ni][nj] = [ci,cj]
    return False

def bomb(si,sj,ei,ej):
    D = arr[si][sj]
    arr[ei][ej] = max(0,arr[ei][ej]-D)
    fset.add((ei,ej))
    for ni, nj in ((ei-1,ej),(ei-1,ej+1),(ei,ej+1),(ei+1,ej+1),(ei+1,ej),(ei+1,ej-1),(ei,ej-1),(ei-1,ej-1)):
        ni,nj = ni%N, nj%M
        arr[ni][nj] = max(0,arr[ei][ej]-D//2)
        fset.add((ni,nj))

for T in range(1,K+1):

    # 1. 공격자 선정
    mn, mn_turn, si, sj = 5001,0,N,M
    for i in range(N):
        for j in range(M):
            # 공격력 가장 작은, 가장 최근에 공격한, 행곽 열의 합이 큰, 열 값이 큰
            if arr[i][j] == 0: continue # 부서진 포탑은 continue
            if arr[i][j] < mn or (arr[i][j] == mn and turn[i][j] < mn_turn) or \
                (arr[i][j] == mn and turn[i][j] == mn_turn and (i + j) < (ei + ej)) or \
                (arr[i][j] == mn and turn[i][j] == mn_turn and (i + j) == (ei + ej) and (j < ej)):
                mn, mn_turn, si, sj = arr[i][j], turn[i][j], i, j

    # 2. 공격대상 선정
    mx, mx_turn, ei, ej = 0, 1001, N, M
    for i in range(N):
        for j in range(M):
            # 공격력 가장 작은, 가장 최근에 공격한, 행곽 열의 합이 큰, 열 값이 큰
            if arr[i][j] == 0: continue  # 부서진 포탑은 continue
            if arr[i][j] > mx or (arr[i][j] == mx and turn[i][j] > mx_turn) or \
                (arr[i][j] == mx and turn[i][j] == mx_turn and (i + j) > (si + sj)) or \
                (arr[i][j] == mx and turn[i][j] == mx_turn and (i + j) == (si + sj) and (j > sj)):
                mx, mx_turn, ei, ej = arr[i][j], turn[i][j], i, j

    arr[si][sj] += (N+M)
    turn[si][sj] = T
    fset = set()
    fset.add((si,sj))
    # 3. 레이저 공격 및 포탄 공격(실패하면 포탄 공격)
    if not laser(si,sj,ei,ej):
        bomb(si,sj,ei,ej)

    cnt = N*M
    for lst in arr:
        cnt -= lst.count(0)
    if cnt <= 1:
        break

    # 4. 포탑 정비
    for i in range(N):
        for j in range(M):
            if arr[i][j] >= 1 and (i,j) not in fset:
                arr[i][j] += 1
print(max(map(max,arr)))