N,M,P,C,D = map(int,input().split())

arr = [[0] * N for _ in range(N)]

ri,rj = map(lambda x: int(x)-1, input().split())
arr[ri][rj] = -1 # 루돌프는 -1로 지정

santa = {}

for _ in range(P):
    idx,i,j = map(int,input().split())
    santa[idx] = (i-1,j-1)
    arr[i-1][j-1] = idx

stun = [0] * (P+1)
live = [True] * (P+1)
live[0] = False
scores = [0] * (P+1)

from collections import deque
def santa_move(num,si,sj,di,dj,mul):
    q = deque()
    q.append((num,si,sj,mul))

    while q:
        cur,ci,cj,mul = q.popleft()
        ni,nj = ci + di*mul, cj + dj*mul

        if 0<=ni<N and 0<=nj<N: # 범위 내 이면
            if arr[ni][nj] == 0: # 빈칸이거나
                arr[ni][nj] = cur
                santa[cur] = (ni,nj)
                return

            elif arr[ni][nj] > 0: # 산타가 있으면
                q.append((arr[ni][nj],ni,nj,1)) # 1칸 연쇄이동
                arr[ni][ni] = cur
                santa[cur] = (ni,nj)

        else: # 범위 밖이면
            live[cur] = False
            return



for turn in range(1,M+1):
    # [1] 루돌프 움직임
    # [1-1-1] 가장 가까운 산타 선정(탈락 x 산타)
    min_dist = 2*N**2
    for idx in range(1,P+1):
        if not live[idx]: continue # 탈락한 산타 건너뛰기
        si,sj = santa[idx]
        dist = (ri-si)**2 + (rj-sj)**2
        if min_dist > dist: # 가장 가까운 산타 선정
            min_dist = dist
            tlst = [(si,sj,idx)]
        elif min_dist == dist: # [1-1-2]가까운 산타 2명 이상
            tlst.append((si,sj,idx))

    if len(tlst) >=2: # r좌표가 큰, c좌표가 큰
        tlst.sort(reverse=True)
    si,sj,mn_idx = tlst[0] # 가장 가까운 산타 선정 완료

    # [1-2] 8방향 이동
    rdi, rdj = 0, 0
    if ri > si: rdi = -1
    elif ri < si : rdi = 1

    if rj > sj : rdj = -1
    elif rj < sj : rdj = 1

    # 이동처리
    arr[ri][rj] = 0
    ri,rj = ri+rdi, rj+rdj
    arr[ri][rj] = -1

    # [1-3] 루돌프의 충돌
    if (ri,rj) == (si,sj):
        stun[mn_idx] = turn+2
        scores[mn_idx] += C
        santa_move(mn_idx,si,sj,rdi,rdj,C)

    # [2] 산타 이동
    for idx in range(1,P+1):
        if not live[idx] : continue # 탈락한 산타 건너뛰기
        if stun[idx] > turn: continue # 기절해있으면 건너뛰기

        # [2-1] 가장 가까워지는 방향으로 이동
        si,sj = santa[idx]
        min_dist = (ri-si) ** 2 + (rj-sj) ** 2
        mlst = []
        for di,dj in ((-1,0),(0,1),(1,0),(0,-1)):
            ni,nj = si+di,sj+dj
            dist = (ri-ni) ** 2 + (rj-nj) ** 2
            if 0<=ni<N and 0<=nj<N and arr[ni][nj] <= 0 and min_dist > dist:
                min_dist = dist
                mlst.append((ni,nj,di,dj))
        if not mlst: # 없으면 건너뛰기
            continue
        ni,nj,di,dj = mlst[-1] # 가장 마지막에 쌓인게 짧은 거리
        arr[si][sj] = 0  # 이동 처리

        # [2-2-1] 산타 충돌
        if (ni,nj) == (ri,rj):
            stun[idx] = turn + 2
            scores[idx] += D
            santa_move(idx,ni,nj,-di,-dj,D)

        # [2-2-2] 빈칸 이면
        else:
            arr[ni][nj] = idx
            santa[idx] = (ni,nj)

    if live.count(True) == 0: break

    for i in range(1,P+1):
        if live[i]:
            scores[i] += 1

for i in range(1,P+1):
    print(scores[i], end=' ')