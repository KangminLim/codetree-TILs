N, M, K = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]
turn = [[0] * M for _ in range(N)]


from collections import deque
def laser(si,sj,ei,ej):
    q = deque()
    q.append((si,sj))
    v = [[[] for _ in range(M)] for _ in range(N)]
    v[si][sj] = (si,sj)
    D = arr[si][sj]
    while q:
        ci,cj = q.popleft()
        if (ci,cj) == (ei,ej):
            arr[ei][ej] = max(0,arr[ei][ej]-D)
            while True:
                ci,cj = v[ci][cj]
                if (ci,cj) == (si,sj):
                    return True
                arr[ci][cj] = max(0,arr[ci][cj]-D//2)
                fset.add((ci,cj))
        else:
            for di,dj in ((0,1),(1,0),(0,-1),(-1,0)):
                ni,nj = (ci+di)%N,(cj+dj)%M
                if arr[ni][nj] != 0 and not v[ni][nj]:
                    q.append((ni,nj))
                    v[ni][nj] = (ci,cj)

    return False

def bomb(si,sj,ei,ej):
    D = arr[si][sj]
    arr[ei][ej] = max(0,arr[ei][ej]-D)
    for di,dj in ((-1,-1),(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1)):
        ni,nj = (ei+di)%N, (ej+dj)%M
        if (ni,nj) != (si,sj):
            arr[ni][nj] = max(0,arr[ni][nj]-D//2)
            fset.add((ni,nj))

for T in range(1,K+1):
    # 1. 공격자 선정 : 부서지지 않은 포탑 중 가장 약한 포탑이 공격자로 선정된다.
    mn,mn_turn,si,sj = 5001,0,-1,-1
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 0: continue # 부서진 포탑 제외
            if mn > arr[i][j] or (mn==arr[i][j] and mn_turn < turn[i][j]) or \
                (mn == arr[i][j] and mn_turn == turn[i][j] and i+j > si+sj) or \
                (mn == arr[i][j] and mn_turn == turn[i][j] and i + j == si + sj and j > sj):
                mn,mn_turn,si,sj = arr[i][j],turn[i][j],i,j

    # 2. 공격 대상 선정 : 자신을 제외한 가장 강한 포탑 선정
    mx, mx_turn, ei, ej = -1, 1001, 0, 0
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 0: continue  # 부서진 포탑 제외
            if mx < arr[i][j] or (mx == arr[i][j] and mx_turn > turn[i][j]) or \
                    (mx == arr[i][j] and mx_turn == turn[i][j] and i + j < ei + ej) or \
                    (mx == arr[i][j] and mx_turn == turn[i][j] and i + j == ei + ej and j < ej):
                mx, mx_turn, ei, ej = arr[i][j], turn[i][j], i, j

    turn[si][sj] = T
    arr[si][sj] += (N+M)

    fset = set()
    fset.add((si, sj))
    fset.add((ei, ej))

    if not laser(si,sj,ei,ej):
        bomb(si,sj,ei,ej)

    cnt = N*M
    for a in arr:
        cnt -= a.count(0)
    if cnt <= 1: break

    for i in range(N):
        for j in range(M):
            if arr[i][j] > 0 and (i,j) not in fset:
                arr[i][j] += 1

print(max(map(max,arr)))