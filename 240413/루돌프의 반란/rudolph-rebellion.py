N, M, P, C, D = map(int,input().split())
arr = [[0] * N for _ in range(N)]
ri,rj = map(lambda x:int(x)-1, input().split())
arr[ri][rj] = -1
santa = {}

is_live = [True] * (P+1)
is_live[0] = False
is_stun = [0] * (P+1)
scores = [0] * (P+1)

for _ in range(P):
    idx,si,sj = map(int,input().split())
    santa[idx] = [si-1,sj-1]
    arr[si-1][sj-1] = idx

from collections import deque

def santa_move(start,si,sj,di,dj,mul):
    q = deque()
    q.append((start,si,sj,mul))

    while q:
        cur, ci, cj, mul = q.popleft()
        ni,nj = ci+di*mul, cj+dj*mul
        if 0<=ni<N and 0<=nj<N:
            if arr[ni][nj] == 0:
                santa[cur] = [ni, nj]
                arr[ni][nj] = cur
                return
            else:
                q.append((arr[ni][nj],ni,nj,1))
                santa[cur] = [ni,nj]
                arr[ni][nj] = cur
        else:
            is_live[cur] = False
            return


for turn in range(1,M+1):
    # 모두 탈락 시 종료
    if is_live.count(True) == 0: break

    min_dist = 2*N**2
    # [1] 루돌프는 가장 가까운 산타를 향해 1칸 돌진
    # [1-1] 가장 가까운 산타 찾기
    for idx in range(1,P+1):
        if not is_live[idx]: continue

        si,sj = santa[idx]
        dist = (ri-si)**2 + (rj-sj)**2

        if min_dist > dist:
            min_dist = dist
            tlst = [(si,sj,idx)]
        elif min_dist == dist:
            tlst.append((si,sj,idx))

    if len(tlst) > 1:
        tlst.sort(reverse=True)

    si,sj,mn_idx = tlst[0] # 행, 열 우선 순위

    # [1-2] 8방향 이동
    rdi, rdj = 0, 0

    if ri>si : rdi = -1
    elif ri<si : rdi = 1

    if rj>sj : rdj = -1
    elif rj<sj : rdj = 1

    arr[ri][rj] = 0
    ri,rj = ri+rdi, rj+rdj
    arr[ri][rj] = -1

    if (ri,rj) == (si,sj):
        is_stun[mn_idx] = turn + 2
        scores[mn_idx] += C
        santa_move(mn_idx,si,sj,rdi,rdj,C)

    # [2] 산타는 루돌프에게 가장 가까워지는 방향으로 1칸 이동
    for idx in range(1,P+1):
        if not is_live[idx] : continue
        if is_stun[idx] > turn: continue

        si,sj = santa[idx]
        min_dist = (ri-si)**2 + (rj-sj)**2
        tlst = []
        for di,dj in ((-1,0),(0,1),(1,0),(0,-1)):
            ni,nj = si+di, sj+dj
            dist = (ri-ni)**2 + (rj-nj)**2
            if 0<=ni<N and 0<=nj<N and arr[ni][nj] <= 0 and min_dist > dist:
                min_dist = dist
                tlst.append((ni,nj,di,dj))
        if not tlst: continue

        arr[si][sj] = 0
        # 가장 맨 마지막에 쌓인 tlst가 최단거리
        ni,nj,di,dj = tlst[-1]

        # 충돌하면
        if (ni,nj) == (ri,rj):
            is_stun[idx] = turn + 2
            scores[idx] += D
            santa_move(idx,ni,nj,-di,-dj,D)

        else:
            santa[idx] = [ni,nj]
            arr[ni][nj] = idx

    for idx in range(1,P+1):
        if is_live[idx]:
            scores[idx] += 1


for idx in range(1,P+1):
    print(scores[idx], end=' ')