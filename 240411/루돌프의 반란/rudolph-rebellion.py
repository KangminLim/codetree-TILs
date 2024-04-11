N,M,P,C,D = map(int,input().split())

arr = [[0] * N for _ in range(N)]

ri,rj = map(lambda x: int(x)-1,input().split())
arr[ri][rj] = -1

santa = {}

for _ in range(P):
    idx, i, j = map(int,input().split())
    santa[idx] = [i-1,j-1]
    arr[i-1][j-1] = idx

is_stun = [0] * (P+1)
is_live = [True] * (P+1)
is_live[0] = False
scores = [0] * (P+1)

from collections import deque

def santa_move(cur,ci,cj,di,dj,mul):
    q = deque()
    q.append((cur,ci,cj,mul))

    while q:
        cur,ci,cj,mul = q.popleft()
        ni, nj = ci+di*mul, cj+dj*mul
        if 0<=ni<N and 0<=nj<N:
            if arr[ni][nj] > 0:
                q.append((arr[ni][nj],ni,nj,1))
                arr[ni][nj] = cur
                santa[cur] = [ni,nj]
            else:
                arr[ni][nj] = cur
                santa[cur] = [ni, nj]
                return
        else:
            is_live[cur] = False
            return

for turn in range(1,M+1):
    if is_live.count(True) == 0 : break
    mn_dist = 2*N**2
    for idx in santa:
        if not is_live[idx] : continue
        si,sj = santa[idx]
        dist = (ri-si)**2 + (rj-sj)**2
        if mn_dist > dist:
            mn_dist = dist
            tlst = [(si,sj,idx)]
        elif mn_dist == dist:
            tlst.append((si,sj,idx))
    if len(tlst)>1:
        tlst.sort(reverse=True)
    si,sj,mn_idx = tlst[0]

    rdi, rdj = 0, 0
    if ri > si: rdi = -1
    elif ri < si : rdi = 1

    if rj > sj : rdj = -1
    elif rj < sj : rdj = 1

    # 이동 처리(이동 전)
    arr[ri][rj] = 0
    ri,rj = ri+rdi,rj+rdj
    # 이동 처리(이동 후)
    arr[ri][rj] = -1

    # 충돌하면
    if (ri,rj) == (si,sj):
        scores[mn_idx] += C
        is_stun[mn_idx] = turn + 2
        santa_move(mn_idx,si,sj,rdi,rdj,C)

    for idx in santa:
        if not is_live[idx] : continue
        if is_stun[idx] > turn : continue

        si,sj = santa[idx]
        min_dist = (ri-si)**2 + (rj-sj)**2
        mlst = []

        for di, dj in ((-1,0),(0,1),(1,0),(0,-1)):
            ni,nj = si+di,sj+dj
            dist = (ri-ni)**2 + (rj-nj)**2
            if 0<=ni<N and 0<=nj<N and arr[ni][nj] <= 0 and min_dist > dist:
                min_dist = dist
                mlst.append((ni,nj,di,dj))

        if not mlst: continue

        arr[si][sj] = 0
        ni,nj,di,dj = mlst[-1]

        if (ri,rj) == (ni,nj):
            scores[idx] += D
            is_stun[idx] = turn + 2
            santa_move(idx,ni,nj,-di,-dj,D)

        else:
            arr[ni][nj] = idx
            santa[idx] = [ni,nj]

    for idx in santa:
        if is_live[idx]:
            scores[idx] += 1

print(*scores[1:])