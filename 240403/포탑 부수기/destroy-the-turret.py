N, M, K = map(int,input().split())
arr =[list(map(int,input().split())) for _ in range(N)]
turn = [[0] * M for _ in range(N)]

from collections import deque
def bfs(si,sj,ei,ej):
    q = deque()
    q.append((si,sj))
    v = [[[] for _ in range(M)] for _ in range(N)]
    v[si][sj] = (si,sj)
    d = arr[si][sj]

    while q:
        ci,cj = q.popleft()
        if (ci,cj) == (ei,ej):
            arr[ei][ej] = max(0,arr[ei][ej]-d)
            while True:
                ci,cj = v[ci][cj]
                if (ci,cj) == (si,sj):
                    return True
                arr[ci][cj] = max(0,arr[ci][cj]-d//2)
                fset.add((ci,cj))

        for di,dj in ((0,1),(1,0),(0,-1),(-1,0)):
            ni, nj = (ci + di)%N,  (cj + dj)%M
            if not v[ni][nj] and arr[ni][nj] >0:
                q.append((ni,nj))
                v[ni][nj] = (ci,cj) # 방문 기록을 남기기
    return False

def bomb(si,sj,ei,ej):
    d = arr[si][sj]
    arr[ei][ej] = max(0,arr[ei][ej]-d)
    for di,dj in ((0,-1),(-1,-1),(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1)):
        ni,nj = (ei+di)%N, (ej+dj)%M
        if (ni,nj) != (si,sj):
            arr[ni][nj] = max(0,arr[ni][nj]-d//2)
            fset.add((ni,nj))

for T in range(1,K+1):
    # [1] 공격자 선정
    mn, mx_turn, si,sj = 5001, 0, -1, -1
    for i in range(N):
        for j in range(M):
            if arr[i][j] <= 0:
                continue
            # 공격력 가장 낮은, 가장 최근에 공격한 포탑, 행과 열의 합이 가장 큰, 열 값이 가장 큰
            if arr[i][j] < mn or (arr[i][j]==mn and mx_turn<turn[i][j]) or \
                (arr[i][j] == mn and mx_turn==turn[i][j] and si+sj < i+j) or \
                (arr[i][j] == mn and mx_turn==turn[i][j] and si+sj ==  i+j and sj < j):
                mn , mx_turn, si, sj = arr[i][j], turn[i][j], i, j

    # [2] 공격 대상자 선정
    mx, mn_turn, ei,ej = -1, 1001, 11, 11
    for i in range(N):
        for j in range(M):
            if arr[i][j] <= 0: continue
            # 공격력 가장 높은, 가장 공격한지 오래된 포탑, 행과 열의 합이 가장 작은, 열 값이 가장 작은
            if arr[i][j] > mx or (arr[i][j]==mx and mn_turn>turn[i][j]) or \
                (arr[i][j] == mx and mn_turn==turn[i][j] and ei+ej > i+j) or \
                (arr[i][j] == mx and mn_turn==turn[i][j] and ei+ej ==  i+j and ej > j):
                mx , mn_turn, ei, ej = arr[i][j], turn[i][j], i, j

    # [3] 공격자 공격력 상승
    arr[si][sj] += (N+M)
    turn[si][sj] = T # 턴 기록
    fset = set() # 공격과 무관했던 포탑을 기록하기 위해 fset 선언
    fset.add((si,sj))
    fset.add((ei,ej))

    if bfs(si,sj,ei,ej) == False:
        bomb(si,sj,ei,ej) # 포탄 공격

    for i in range(N):
        for j in range(M):
            if (i,j) not in fset and arr[i][j] > 0:
                arr[i][j] += 1

    cnt = M*N
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 0:
                cnt -=1
    if cnt <= 1:
        break


print(max(map(max,arr)))