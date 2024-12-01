N, M, K = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]

turn = [[0] * M for _ in range(N)]

from collections import deque
def laser(si,sj,ei,ej):
    q = deque()
    q.append((si,sj))
    D = arr[si][sj]
    v = [[[] for _ in range(M)] for _ in range(N)]
    v[si][sj] = [si,sj]
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

        else:
            for ni,nj in ((ci,cj+1),(ci+1,cj),(ci,cj-1),(ci-1,cj)):
                ni,nj = ni%N, nj%M
                if arr[ni][nj] > 0 and not v[ni][nj]:
                    q.append((ni,nj))
                    v[ni][nj] = [ci,cj]

def bomb(si,sj,ei,ej):
    D = arr[si][sj]
    arr[ei][ej] = max(0,arr[ei][ej] - D)

    for ni,nj in ((ei-1,ej-1),(ei-1,ej),(ei-1,ej+1),(ei,ej+1),(ei+1,ej+1),(ei+1,ej),(ei+1,ej-1),(ei,ej-1)):
        ni,nj = ni%N, nj%M
        if (ni,nj) != (si,sj):
            arr[ni][nj] = max(0, arr[ni][nj] - D//2)
            fset.add((ni,nj))



for t in range(1,K+1):

    # 1. 공격자 선정
    mn, mx_turn, si, sj = 5001, 0, 11, 11
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 0: continue
            if arr[i][j] < mn or (arr[i][j] == mn and turn[i][j] > mx_turn) or \
                (arr[i][j] == mn and turn[i][j] == mx_turn and (i+j) > (si+sj)) or \
                 (arr[i][j] == mn and turn[i][j] == mx_turn and (i+j) == (si+sj) and (j > sj)):
                mn, mx_turn, si, sj = arr[i][j], turn[i][j], i, j

    # 2. 공격 대상 선정
    mx, mn_turn, ei, ej = -1, 1001, 3, 3
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 0: continue
            if arr[i][j] > mx or (arr[i][j] == mx and turn[i][j] < mn_turn) or \
                (arr[i][j] == mx and turn[i][j] == mn_turn and (i + j) < (ei + ej)) or \
                (arr[i][j] == mx and turn[i][j] == mn_turn and (i + j) == (ei + ej) and (j < ej)):
                mx, mn_turn, ei, ej = arr[i][j], turn[i][j], i, j
    # print('')

    # 3. 공격자 업데이트
    arr[si][sj] += (N+M)
    turn[si][sj] = t
    fset = set()
    fset.add((si,sj))
    fset.add((ei, ej))

    # 4. 공격
    if not laser(si,sj,ei,ej):
        bomb(si,sj,ei,ej)
    # print('')

    # 종료 조건
    cnt = N*M
    for lst in arr:
        cnt -= lst.count(0)
    if cnt == 1: break

    # 5. 포탑 정비
    for i in range(N):
        for j in range(M):
            if arr[i][j] > 0 and (i,j) not in fset:
                arr[i][j] += 1
    # print('')
ans = max(map(max,arr))
print(ans)