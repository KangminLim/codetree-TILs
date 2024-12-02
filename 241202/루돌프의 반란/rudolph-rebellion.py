N,M,P,C,D = map(int,input().split())

arr = [[0] * N for _ in range(N)]

ri,rj = map(lambda x:int(x)-1,input().split())
arr[ri][rj] = -1

santa = {}

for _ in range(P):
    idx,ci,cj = map(int,input().split())
    santa[idx] = [ci-1,cj-1]
    arr[ci-1][cj-1] = idx

live = [True] * (P+1)
live[0] = False
stun = [0] * (P+1)
score = [0] * (P+1)

di,dj = [-1,0,1,0],[0,1,0,-1]

from collections import deque
def santa_move(sidx,si,sj,di,dj,mul):
    q = deque()
    q.append((sidx,si,sj,mul))

    while q:
        cur,ci,cj,mul = q.popleft()
        ni,nj = ci+di*mul,cj+dj*mul
        if 0<=ni<N and 0<=nj<N:
            if arr[ni][nj] > 0:
                q.append((arr[ni][nj],ni,nj,1))
                arr[ni][nj] = cur
                santa[cur] = [ni,nj]
            else:
                arr[ni][nj] = cur
                santa[cur] = [ni,nj]
        else:
            live[cur] = False

for t in range(1,M+1):

    # 종료 조건
    if live.count(True) == 0: break

    mn_dist = 2*N*N
    # 1. 루돌프 이동
    for idx in range(1,P+1):
        if not live[idx]: continue
        si,sj = santa[idx]
        dist = (ri-si)**2 + (rj-sj)**2
        if mn_dist > dist:
            mn_dist = dist
            tlst = [(idx,si,sj)]
        elif mn_dist == dist:
            tlst.append((idx,si,sj))

    tlst.sort(key=lambda x:(-x[1],-x[2]))
    tidx,ti,tj = tlst[0]

    rdi,rdj = 0,0
    if ri > ti:
        rdi = -1
    elif ri < ti:
        rdi = 1

    if rj > tj:
        rdj = -1
    elif rj < tj:
        rdj = 1

    arr[ri][rj] = 0
    ri,rj = ri+rdi, rj+rdj
    arr[ri][rj] = -1

    # 충돌(루돌프에 의한)
    if (ri,rj) == (ti,tj):
        stun[tidx] = t+2
        score[tidx] += C
        santa_move(tidx,ri,rj,rdi,rdj,C)

    # 2. 산타 이동
    for idx in range(1,P+1):
        if not live[idx]: continue
        if stun[idx] > t: continue
        tlst = []
        ci,cj = santa[idx]
        mn_dist = (ri-ci)**2 + (rj-cj)**2
        for di,dj in ((-1,0),(0,1),(1,0),(0,-1)):
            ni,nj = ci+di,cj+dj
            if 0<=ni<N and 0<=nj<N and arr[ni][nj] <= 0 and mn_dist > (ri-ni)**2 + (rj-nj)**2:
                mn_dist = (ri-ni)**2 + (rj-nj)**2
                tlst.append((ni,nj,di,dj))
        if not tlst:
            continue
        ni,nj,di,dj = tlst[-1]
        arr[ci][cj] = 0
        if (ni,nj) == (ri,rj):
            stun[idx] = t + 2
            score[idx] += D
            santa_move(idx, ni, nj, -di, -dj, D)
        else:
            santa[idx] = (ni, nj)
            arr[ni][nj] = idx

    for idx in range(1,P+1):
        if live[idx]:
            score[idx] += 1
    # print('')
print(*score[1:])