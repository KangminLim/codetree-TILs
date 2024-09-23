N, M, P, C, D = map(int,input().split())
ri,rj = map(lambda x:int(x)-1,input().split())
santa = {}
arr = [[0] * N for _ in range(N)]
arr[ri][rj] = -1

for _ in range(P):
    idx, si, sj = map(int,input().split())
    santa[idx] = [si-1,sj-1]
    arr[si-1][sj-1] = idx

is_stun = [0] * (P+1)
is_live = [True] * (P+1)
is_live[0] = False
scores = [0] * (P+1)

from collections import deque
def santa_move(cur,si,sj,di,dj,mul):
    q = deque()
    q.append((cur,si,sj,mul))
    while q:
        idx,ci,cj,mul = q.popleft()
        ni,nj = ci+di*mul, cj+dj*mul
        # 범위 내
        if 0<=ni<N and 0<=nj<N:
            if arr[ni][nj] > 0:
                q.append((arr[ni][nj],ni,nj,1))
            arr[ni][nj] = idx
            santa[idx] = [ni,nj]
        else:
            is_live[idx] = False
            return

for turn in range(1,M+1):

    if is_live.count(True) == 0: break
    # 1. 루돌프의 이동
    dist = N*N*2
    for idx in range(1,P+1):
        if not is_live[idx]: continue
        ci,cj = santa[idx]
        # 1.1 가까운 산타 찾기(r좌표 큰, c좌표 큰)
        if dist > (ri-ci)**2 + (rj-cj)**2:
            dist = (ri-ci)**2 + (rj-cj)**2
            tlst = [(idx,ci,cj)]
        elif dist == (ri-ci)**2 + (rj-cj)**2:
            tlst.append((idx,ci,cj))
    tlst.sort(key=lambda x:(-x[1],-x[2]))
    sidx,si,sj = tlst[0]

    rdi, rdj = 0, 0
    if si > ri:
        rdi = 1
    elif si < ri:
        rdi = -1

    if sj > rj:
        rdj = 1
    elif sj < rj:
        rdj = -1

    arr[ri][rj] = 0
    ri,rj = ri+rdi, rj+rdj

    # 1.2.1 산타가 있으면
    if arr[ri][rj] > 0:
        santa_move(sidx,si,sj,rdi,rdj,C)
        scores[sidx] += C
        is_stun[sidx] = turn + 2

    arr[ri][rj] = -1

    # 2. 산타의 이동
    for idx in range(1,P+1):
        if not is_live[idx] or is_stun[idx] > turn: continue
        ci,cj = santa[idx]
        dist = (ri-ci)**2 + (rj-cj)**2
        tlst = []
        for di,dj in ((-1,0),(0,1),(1,0),(0,-1)):
            ni,nj = ci+di,cj+dj
            if 0<=ni<N and 0<=nj<N and arr[ni][nj] <= 0:
                if dist > (ri-ni)**2 + (rj-nj)**2:
                    dist = (ri-ni)**2 + (rj-nj)**2
                    tlst.append((ni,nj,di,dj))
        if not tlst: continue
        ni,nj,di,dj = tlst[-1]
        arr[ci][cj] = 0
        # 2.1 루돌프 있으면 충돌
        if arr[ni][nj] == -1:
            santa_move(idx,ni,nj,-di,-dj,D)
            scores[idx] += D
            is_stun[idx] = turn + 2
        # 2.2 루돌프 없으면
        else:
            arr[ni][nj] = idx
            santa[idx] = [ni,nj]

    for idx in range(1,P+1):
        if is_live[idx]:
            scores[idx] += 1
print(*scores[1:],end=' ')