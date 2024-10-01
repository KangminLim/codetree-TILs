N,M,P,C,D = map(int,input().split())

arr = [[0] * N for _ in range(N)]

ri,rj = map(lambda x:int(x)-1,input().split())
arr[ri][rj] = -1
santa = {}
for _ in range(1,P+1):
    idx,si,sj = map(lambda x:int(x)-1,input().split())
    santa[idx+1] = (si,sj)
    arr[si][sj] = idx+1

is_stun = [0] * (P+1)
is_live = [True] * (P + 1)
is_live[0] = False
scores = [0] * (P+1)

from collections import deque
def santa_move(cur,si,sj,di,dj,mul):
    q = deque()
    q.append((cur,si,sj,mul))

    while q:
        cur,ci,cj,mul = q.popleft()
        ni,nj = ci+di*mul,cj+dj*mul

        if 0<=ni<N and 0<=nj<N:
            if arr[ni][nj] > 0:
                q.append((arr[ni][nj],ni,nj,1))
                arr[ni][nj] = cur
                santa[cur] = (ni,nj)
            else:
                arr[ni][nj] = cur
                santa[cur] = (ni, nj)
                return

        else:
            is_live[cur] = False
            return

for turn in range(1,M+1):
    if is_live.count(False) == P+1: break
    mx_dist = N*N*2
    # print('')
    # 1. 루돌프 이동
    for idx in range(1,P+1):
        if not is_live[idx] : continue
        ci,cj = santa[idx]
        dist = (ri-ci)**2 + (rj-cj)**2
        if dist < mx_dist:
            mx_dist = dist
            tlst = [(idx,ci,cj)]
        elif dist == mx_dist:
            tlst.append((idx,ci,cj))
    tlst.sort(key=lambda x:(-x[1],-x[2]))
    sidx,si,sj = tlst[0]
    # print('')


    rdi,rdj = 0,0
    if ri > si: rdi = -1
    elif ri < si: rdi = 1

    if rj > sj: rdj = -1
    elif rj < sj: rdj = 1

    arr[ri][rj] = 0
    ri, rj = ri+rdi, rj+rdj
    arr[ri][rj] = -1
    # 빈칸이 아니면
    if (ri,rj) == (si,sj):
        santa_move(sidx,ri,rj,rdi,rdj,C)
        is_stun[sidx] = turn + 2
        scores[sidx] += C

    # 2. 산타 움직임
    for idx in santa:
        if not is_live[idx] or is_stun[idx] > turn: continue
        ci,cj = santa[idx]
        tlst = []
        dist = (ri-ci)**2 + (rj-cj)**2
        # for ni,nj in ((ci-1,cj),(ci,cj+1),(ci+1,cj),(ci,cj-1)):
        for di,dj in ((-1,0),(0,1),(1,0),(0,-1)):
            ni,nj = ci+di,cj+dj
            if 0<=ni<N and 0<=nj<N and arr[ni][nj] <=0 and dist > (ri-ni)**2 + (rj-nj)**2:
                dist = (ri-ni)**2 + (rj-nj)**2
                tlst.append((ni,nj,di,dj))
        if tlst:
            ni,nj,di,dj = tlst[-1]
            arr[ci][cj] = 0

            if (ni,nj) == (ri,rj):
                santa_move(idx,ni,nj,-di,-dj,D)
                is_stun[idx] = turn + 2
                scores[idx] += D

            else:
                arr[ni][nj] = idx
                santa[idx] = (ni,nj)

    for idx in santa:
        if is_live[idx]:
            scores[idx] += 1

    # print('')
print(*scores[1:])