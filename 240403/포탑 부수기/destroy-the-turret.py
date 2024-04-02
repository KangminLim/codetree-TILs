N, M, K = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]
turn = [[0] * M for _ in range(N)]

from collections import deque
def bfs(si,sj,ei,ej):
    q = deque()
    v = [[[] for _ in range(M)] for _ in range(N)] # 방문 경로
    v[si][sj] = (si,sj)
    q.append((si,sj))
    d = arr[si][sj] # 데미지
    while q:
        ci,cj = q.popleft()
        if (ci,cj) == (ei,ej): # 종료 조건
            arr[ei][ej] = max(0,arr[ei][ej]-d)
            while True:
                ci,cj = v[ci][cj]
                if (ci,cj) == (si,sj):
                    return True
                fset.add((ci,cj))
                arr[ci][cj] = max(0,arr[ci][cj]-d//2)
        for di,dj in ((-1,0),(0,1),(1,0),(0,-1)):
            ni,nj = (ci+di)%N, (cj+dj)%M
            if not v[ni][nj] and arr[ni][nj] >0: # 방문한적 없고, 벽이 아니면
                q.append((ni,nj))
                v[ni][nj] = (ci,cj)
    return False

def bomb(si,sj,ei,ej):
    d = arr[si][sj] # 데미지
    arr[ei][ej] = max(0, arr[ei][ej]-d)

    for di,dj in ((-1,-1),(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1)):
        ni, nj = (si+di)%N ,(sj+dj)%M
        if arr[ni][nj] > 0:
            arr[ni][nj] = max(0, arr[ni][nj]-d//2)
            fset.add((ni,nj))

for T in range(1,K+1):
    # 완전탐색
    # [1] 공격자 선정
    mn, mx_turn, si, sj = 5001, 0, -1, -1
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 0: continue
            #  [1-1] 공격력이 가장 낮은, 가장 최근에 공격한 포탑, 행과 열의 합이 가장 큰, 열 값이 가장 큰
            if arr[i][j] < mn or (arr[i][j] == mn and mx_turn < turn[i][j]) or \
                (arr[i][j] == mn and mx_turn == turn[i][j] and si+sj < i+j) or \
                (arr[i][j] == mn and mx_turn == turn[i][j] and si+sj == i+j and sj<j):
                mn, mx_turn, si,sj = arr[i][j],turn[i][j],i,j

    # [2] 공격 대상 선정
    mx, mn_turn, ei, ej = 0, 1001, 11, 11
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 0: continue
            # [2-1] 공격력이 가장 높은, 마지막으로 공격한 포탑, 행과 열의 합이 가장 작은, 열 값이 가장 작은
            if arr[i][j] > mx or (arr[i][j] == mx and mx_turn > turn[i][j]) or \
                (arr[i][j] == mx and mx_turn == turn[i][j] and si+sj > i+j) or \
                (arr[i][j] == mx and mx_turn == turn[i][j] and si+sj == i+j and sj >j):
                mx, mn_turn, ei, ej = arr[i][j], turn[i][j], i, j

    arr[si][sj] += (M+N)  # 공격자 공격력 증가
    turn[si][sj] = T
    fset = set()
    fset.add((si,sj))
    fset.add((ei,ej))

    if bfs(si,sj,ei,ej) == False:
        bomb(si,sj,ei,ej)

    # 포탑 정비 -> 무관한 포탑 공격력 1 증가
    for i in range(N):
        for j in range(N):
            if (i,j) in fset: continue
            if arr[i][j] > 0:
                arr[i][j] += 1

    cnt = M*N
    for lst in arr:
        cnt -= lst.count(0)
    if cnt <=1: break

print(max(map(max,arr)))