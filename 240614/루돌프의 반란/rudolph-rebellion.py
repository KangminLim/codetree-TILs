N, M, P, C, D = map(int,input().split())
arr = [[0] * N for _ in range(N)]

ri,rj = map(lambda x:int(x)-1,input().split())
arr[ri][rj] = -1

santa = {}
is_live = [True] * (P+1)
is_stun = [False] * (P+1)
is_live[0] = False
scores = [0] * (P+1)

for _ in range(1,P+1):
    idx, si, sj = map(int,input().split())
    santa[idx] = [si-1,sj-1] # 산타 i, j
    arr[si-1][sj-1] = idx

from collections import deque
def move(idx,si,sj,di,dj,mul):
    q = deque()
    q.append((idx,si,sj,mul))

    while q:
        cidx, ci, cj, mul = q.popleft()
        ni,nj = ci+di*mul, cj+dj*mul
        if 0<=ni<N and 0<=nj<N: # 범위 내
            if arr[ni][nj] > 0: # 다른 산타가 있다면
                q.append((arr[ni][nj],ni,nj,1))
                arr[ni][nj] = cidx
                santa[cidx] = [ni,nj]
            else:
                arr[ni][nj] = cidx
                santa[cidx] = [ni,nj]
                return

        else: # 범위 밖
            is_live[cidx] = False
            return

for turn in range(1,M+1):

    if is_live.count(True) == 0: break

    mn_dist = N*N
    # 가장 가까운 산타 찾기
    for idx in range(1,P+1):
        # 기절한 산타는 out
        if not is_live[idx] : continue
        si,sj = santa[idx]
        dist = (ri-si)**2 + (rj-sj)**2
        if mn_dist > dist:
            mn_dist = dist
            tlst = [(si,sj,idx)]
        elif mn_dist == dist:
            tlst.append((si,sj,idx))

    if len(tlst) >= 2:
        tlst.sort(key=lambda x:(-x[0],-x[1]))

    si,sj,sidx = tlst[0] # 가장 가까운 산타 좌표

    rdi,rdj = 0,0
    # 루돌프 8방향 이동
    if ri > si: rdi = -1
    elif ri < si : rdi = 1

    if rj > sj : rdj = -1
    elif rj < sj : rdj = 1

    arr[ri][rj] = 0
    ri, rj = ri+rdi, rj+rdj
    arr[ri][rj] = -1

    # 루돌프에 의해 충돌
    if (ri,rj) == (si,sj):
        scores[sidx] += C
        is_stun[sidx] = turn + 2
        move(sidx,si,sj,rdi,rdj,C) # idx, i, j, di, dj, mul

    for idx in range(1,P+1):
        if not is_live[idx] : continue
        if is_stun[idx] > turn: continue
        ci,cj = santa[idx]
        slst = []
        dist = (ri-ci)**2 + (rj-cj)**2
        for di,dj in ((-1,0),(0,1),(1,0),(0,-1)): # 상우하좌
            ni,nj = ci+di, cj+dj
            new_dist = (ri-ni)**2+(rj-nj)**2
            if 0<=ni<N and 0<=nj<N and arr[ni][nj] <= 0 and dist > new_dist: # 범위 내, 다른 산타 없고, 거리가 가까워지는
                dist = new_dist
                slst.append((ni,nj,di,dj))

        # 가까워지는 방법이 없다면 다른 산타
        if not slst: continue
        ni,nj,di,dj = slst[-1] # 가장 마지막 리스트 요소가 가장 가까워지는 경우
        arr[ci][cj] = 0

        if (ni,nj) == (ri,rj): # 충돌하는 경우
            scores[idx] += D
            is_stun[idx] = turn + 2
            move(idx,ni,nj,-di,-dj,D)
        else: # 충돌 X
            arr[ni][nj] = idx
            santa[idx] = [ni,nj]

    for idx in santa:
        if is_live[idx]:
            scores[idx] += 1


for i in range(1,P+1):
    print(scores[i],end=' ')