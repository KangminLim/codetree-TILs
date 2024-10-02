N,M,K = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]
turn = [[0] * M for _ in range(N)]

from collections import deque
def bfs(si,sj,ei,ej):
    q = deque()
    q.append((si,sj))
    v = [[[]] * M for _ in range(N)]
    v[si][sj] = (si,sj)
    D = arr[si][sj]
    while q:
        ci,cj = q.popleft()
        if (ci,cj) == (ei,ej):
            arr[ci][cj] = max(0, arr[ci][cj] - D)
            while True:
                ci,cj = v[ci][cj]
                if (ci,cj) == (si,sj):
                    return True
                arr[ci][cj] = max(0, arr[ci][cj] - D//2)
                fset.add((ci,cj))

        for di,dj in ((0,1),(1,0),(0,-1),(-1,0)):
            ni,nj = (ci+di)%N,(cj+dj)%M
            if arr[ni][nj] > 0 and not v[ni][nj]:
                q.append((ni,nj))
                v[ni][nj] = (ci,cj)
    return False

def bomb(si,sj,ei,ej):
    D = arr[si][sj]
    arr[ei][ej] = max(0, arr[ei][ej] - D)
    for di, dj in ((-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1)):
        ni, nj = (ei + di) % N, (ej + dj) % M
        if (ni,nj) != (si,sj):
            fset.add((ni, nj))
            arr[ni][nj] = max(0, arr[ni][nj] - D // 2)

for T in range(1,K+1):

    # 1. 공격자 선정
    mn,mx_turn,si,sj = 5001,0,11,11

    for i in range(N):
        for j in range(M):
            if arr[i][j] > 0:
                if mn > arr[i][j] or (mn == arr[i][j] and mx_turn < turn[i][j]) or \
                    (mn == arr[i][j] and mx_turn == turn[i][j] and si+sj < i+j) or \
                    (mn == arr[i][j] and mx_turn == turn[i][j] and si + sj == i + j and sj < j):
                    mn, mx_turn, si, sj = arr[i][j], turn[i][j], i, j

    # 2. 공격대상 선정
    mx,mn_turn,ei,ej = 0,1001,11,11
    for i in range(N):
        for j in range(M):
            if arr[i][j] > 0:
                if mx < arr[i][j] or (mx == arr[i][j] and mn_turn > turn[i][j]) or \
                    (mx == arr[i][j] and mn_turn == turn[i][j] and ei + ej > i + j) or \
                    (mx == arr[i][j] and mn_turn == turn[i][j] and ei + ej == i + j and ej > j):
                    mx, mn_turn, ei, ej = arr[i][j], turn[i][j], i, j
    # print('')
    # 공격력, 공격 턴, fset 갱신
    fset = set()
    fset.add((si,sj))
    fset.add((ei,ej))
    arr[si][sj] += (N+M)
    turn[si][sj] = T

    if not bfs(si,sj,ei,ej):
        bomb(si,sj,ei,ej)
    # print('')
    # 종료 조건
    cnt = N*M
    for lst in arr:
        cnt -= lst.count(0)

    if cnt == 1: break

    for i in range(N):
        for j in range(M):
            if arr[i][j] > 0 and (i,j) not in fset:
                arr[i][j] += 1
    # print('')

print(max(map(max,arr)))