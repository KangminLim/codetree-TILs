N, M, K = map(int,input().split())

arr = [list(map(int,input().split())) for _ in range(N)]

turn = [[0] * M for _ in range(N)]

from collections import deque
def laser(si,sj,ei,ej):
    q = deque()
    q.append((si,sj))
    d = arr[si][sj]
    v = [[[] for _ in range(M)] for _ in range(N)]
    v[si][sj] = (si,sj)
    while q:
        ci,cj = q.popleft()
        if (ci,cj) == (ei,ej): # 목표지점 끝을 갔을 떄
            arr[ei][ej] = max(0, arr[ei][ej] - d)
            while True:
                ci,cj = v[ci][cj]
                if (ci,cj) == (si,sj):
                    return True
                arr[ci][cj] = max(0,arr[ci][cj] -d//2)
                fset.add((ci,cj))
        else:
            for di,dj in ((0,1),(1,0),(0,-1),(-1,0)):
                ni,nj = (ci+di)%N, (cj+dj)%M

                if arr[ni][nj] >0 and not v[ni][nj]:
                    v[ni][nj] = (ci,cj)
                    q.append((ni,nj))

    return False

def bomb(si,sj,ei,ej):
    d = arr[si][sj]
    arr[ei][ej] = max(0,arr[ei][ej]-d)
    for di,dj in ((0,-1),(-1,-1),(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1)):
        ni,nj = (ei+di)%N, (ej+dj)%M
        if (ni,nj) != (si,sj):
            arr[ni][nj] = max(0,arr[ni][nj]-d//2)
            fset.add((ni,nj))


for k in range(1,K+1):
    mn, mx_turn, si,sj = 5001, 0, -1, -1
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 0: continue

            if arr[i][j] < mn or (arr[i][j] == mn and mx_turn < turn[i][j]) or \
                (arr[i][j] == mn and mx_turn == turn[i][j] and si+sj < i+j) or \
                (arr[i][j] == mn and mx_turn == turn[i][j] and si+sj==i+j and sj < j):
                mn,mx_turn,si,sj = arr[i][j],turn[i][j],i,j

    mx, mn_turn, ei,ej = -1, 1001, 11, 11
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 0: continue

            if arr[i][j] > mx or (arr[i][j] == mx and mn_turn > turn[i][j]) or \
                (arr[i][j] == mx and mn_turn == turn[i][j] and ei+ej > i+j) or \
                (arr[i][j] == mx and mn_turn == turn[i][j] and ei+ej==i+j and ej > j):
                mx,mn_turn,ei,ej = arr[i][j],turn[i][j],i,j

    arr[si][sj] += (N+M)
    turn[si][sj] = k

    fset = set()
    fset.add((si,sj))
    fset.add((ei,ej))

    if not laser(si,sj,ei,ej):
        bomb(si,sj,ei,ej)

    cnt = N*M

    for lst in arr:
        cnt -= lst.count(0)
    if cnt <= 1:
        break

    for i in range(N):
        for j in range(M):
            if arr[i][j] >0 and (i,j) not in fset:
                arr[i][j] += 1
mx = 0
for i in range(N):
    for j in range(M):
        mx = max(mx,arr[i][j])
print(mx)