N,M,K = map(int,input().split())

arr = [list(map(int,input().split())) for _ in range(N)]
turn = [[0] * M for _ in range(N)]

from collections import deque
def laser(si,sj,ei,ej):
    q = deque()
    q.append((si,sj))
    v = [[[]] * M for _ in range(N)]
    v[si][sj] = [si,sj]
    d = arr[si][sj]

    while q:
        ci,cj = q.popleft()
        if (ci,cj) == (ei,ej): # 공격지점 도착
            arr[ei][ej] = max(0,arr[ei][ej] - d)
            while True:
                ci,cj = v[ci][cj]
                if (ci,cj) == (si,sj):
                    return True
                fset.add((ci,cj))
                arr[ci][cj] = max(0,arr[ci][cj]-d//2)

        else:
            for ni,nj in ((ci,cj+1),(ci+1,cj),(ci,cj-1),(ci-1,cj)):
                ni, nj = ni%N, nj%M
                if not v[ni][nj] and arr[ni][nj] > 0:
                    q.append((ni,nj))
                    v[ni][nj] = [ci,cj]
    return False

def bomb(si,sj,ei,ej):
    d = arr[si][sj]
    arr[ei][ej] = max(0, arr[ei][ej]-d)

    for ni,nj in ((ei,ej-1),(ei-1,ej-1),(ei-1,ej),(ei-1,ej+1),(ei,ej+1),(ei+1,ej+1),(ei+1,ej),(ei+1,ej-1)):
        ni,nj = ni%N, nj%M

        if (ni,nj) != (si,sj):
            arr[ni][nj] = max(0,arr[ni][nj]-d//2)
            fset.add((ni,nj))

for k in range(1,K+1):

    # [1] 공격자 선정
    # 공격력 가장 낮은, 가장 최근에 공격한 포탑, 행과 열의 합이 가장 큰, 열 값이 가장 큰
    mn, mx_turn, si, sj = 5001, 0, -1, -1
    for i in range(N):
        for j in range(M):
            # 0은 무시
            if arr[i][j] == 0: continue
            if arr[i][j] < mn or (arr[i][j] == mn and turn[i][j] > mx_turn) or \
                (arr[i][j] == mn and turn[i][j] == mx_turn and si+sj < i+j ) or \
                (arr[i][j] == mn and turn[i][j] == mx_turn and si+sj == i+j and sj<j):
                mn,mx_turn,si,sj = arr[i][j], turn[i][j], i, j
    # [2] 공격대상 선정
    # 공격력이 가장 높은, 가장 공격한지 오래된 포탑, 행과 열의 합이 가장 작은, 열 값이 가장 작은
    mx, mn_turn, ei, ej = -1, 1001, 11,11
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 0: continue
            if arr[i][j] > mx or (arr[i][j] == mx and turn[i][j] < mn_turn) or \
                (arr[i][j] == mx and turn[i][j] == mn_turn and ei+ej > i+j) or \
                (arr[i][j] == mx and turn[i][j] == mn_turn and ei+ej == i+j and ej > j ):
                mx,mn_turn,ei,ej = arr[i][j], turn[i][j], i, j

    # 공격자 포탑 / 공격력, 턴 업데이트
    arr[si][sj] += (N+M)
    turn[si][sj] = k

    # 전투에 관련된 집합
    fset = set()
    fset.add((si,sj))
    fset.add((ei,ej))


    if not laser(si,sj,ei,ej):
        bomb(si,sj,ei,ej)

    for i in range(N):
        for j in range(M):
            if arr[i][j] >0 and (i,j) not in fset:
                arr[i][j] += 1

print(max(map(max,arr)))