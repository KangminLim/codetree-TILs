N,M,K = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]
turn = [[0] * M for _ in range(N)]

from collections import deque
def laser(si,sj,ei,ej):
    q = deque()
    q.append((si,sj))
    v = [[[] for _ in range(M)] for _ in range(N)]
    v[si][sj] = [si,sj]
    d = arr[si][sj]

    while q:
        ci,cj = q.popleft()
        if (ci,cj) == (ei,ej):
            arr[ei][ej] = max(0,arr[ei][ej] - d)
            while True:
                ci,cj = v[ci][cj]
                if (ci,cj) == (si,sj):
                    return True
                arr[ci][cj] = max(0,arr[ci][cj] - d//2)
                fset.add((ci,cj))

        else:
            for ni,nj in ((ci,cj+1),(ci+1,cj),(ci,cj-1),(ci-1,cj)):
                ni, nj = ni % N, nj % M
                if arr[ni][nj] > 0 and not v[ni][nj]:
                    q.append((ni,nj))
                    v[ni][nj] = [ci,cj]

    return False

def bomb(si,sj,ei,ej):
    d = arr[si][sj]
    arr[ei][ej] = max(0,arr[ei][ej]-d)
    for ni,nj in ((ei-1,ej),(ei+1,ej),(ei,ej-1),(ei,ej+1),(ei-1,ej-1),(ei+1,ej+1),(ei-1,ej+1),(ei+1,ej-1)):
        ni,nj = ni%N, nj%M
        if (ni,nj) != (si,sj):
            arr[ni][nj] = max(0,arr[ni][nj]-d//2)
            fset.add((ni,nj))

for T in range(1,K+1):
    # N*M 격자 완전 탐색
    mn, mx_turn, si,sj = 5000, 0, 0, 0
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 0: continue
            # 공격력 가장 낮은, 가장 최근에 공격한 포탑, 행과 열의 합이 가장 큰, 열 값이 가장 큰
            if arr[i][j] < mn or (arr[i][j] == mn and turn[i][j] > mx_turn) or \
                (arr[i][j] == mn and turn[i][j] == mx_turn and si+sj < i+j) or \
                (arr[i][j] == mn and turn[i][j] == mx_turn and si+sj == i+j and sj < j):
                mn,mx_turn,si,sj = arr[i][j], turn[i][j], i, j

    mx, mn_turn, ei, ej = 0, 1001, 11, 11
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 0: continue
            # 공격력 가장 높은, 가장 나중에 포탑, 행과 열의 합이 가장 작은, 열 값이 가장 작은
            if arr[i][j] > mx or (arr[i][j] == mx and turn[i][j] < mn_turn) or \
                (arr[i][j] == mx and turn[i][j] == mn_turn and ei + ej > i + j) or \
                (arr[i][j] == mx and turn[i][j] == mn_turn and ei + ej == i + j and ej > j):
                mx, mn_turn, ei, ej = arr[i][j], turn[i][j], i, j

    arr[si][sj] += (M+N)
    turn[si][sj] = T

    fset = set()
    fset.add((si,sj))
    fset.add((ei,ej))

    if not laser(si,sj,ei,ej):
        bomb(si,sj,ei,ej)

    cnt = M*N
    for lst in arr:
        cnt -= lst.count(0)
    if cnt <= 1:
        break

    for i in range(N):
        for j in range(M):
            if (i,j) not in fset and arr[i][j] > 0:
                arr[i][j] += 1

print(max(map(max,arr)))