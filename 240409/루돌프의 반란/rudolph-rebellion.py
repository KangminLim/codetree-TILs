N, M, P, C, D = map(int,input().split())

arr = [[0] * N for _ in range(N)]

ri,rj = map(lambda x:int(x)-1, input().split())
arr[ri][rj] = -1

santa = [[N] * 2 for _ in range(P+1)]
is_stun = [0] * (P+1)
is_live = [True] * (P+1)
is_live[0] = False
scores = [0] * (P+1)


for m in range(1,P+1):
    idx,i,j = map(int,input().split())
    santa[idx] = [i-1,j-1]
    arr[i-1][j-1] = idx

from collections import deque

def santa_move(cur,ci,cj,di,dj,mul):
    q = deque()
    q.append((cur,ci,cj,mul))
    while q:
        cur,ci,cj,mul = q.popleft()
        ni,nj = ci+di*mul, cj+dj*mul
        if 0<=ni<N and 0<=nj<N:
            if arr[ni][nj]>0:
                q.append((arr[ni][nj],ni,nj,1))
                arr[ni][nj] = cur
                santa[cur] = [ni,nj]
            else:
                arr[ni][nj] = cur
                santa[cur] = [ni,nj]
        else:
            is_live[cur] = False
            return

for turn in range(1,M+1):
    if is_live.count(True) ==0: break

    min_dist = 2*N**2
    # [1] 루돌프의 움직임
    # [1-1] 가장 가까운 산타 1명 선택하기
    for idx in range(1,P+1):
        if not is_live[idx]: continue
        si, sj = santa[idx]
        dist = (ri-si)**2 + (rj-sj)**2
        if dist < min_dist:
            min_dist = dist
            tlst = [(si,sj,idx)]
        elif min_dist == dist:
            tlst.append((si,sj,idx))

    if len(tlst) > 1:
        tlst.sort(reverse=True)

    si,sj,mn_num = tlst[0] # 가장 가까운 산타 좌표

    rdi, rdj = 0, 0

    if ri > si: rdi = -1
    elif ri < si: rdi = 1

    if rj > sj : rdj = -1
    elif rj < sj : rdj = 1

    arr[ri][rj] = 0  # 루돌프 이동 처리
    ri, rj = ri+rdi, rj+rdj
    arr[ri][rj] = -1

    if (ri,rj) == (si,sj): # 루돌프 충돌
        is_stun[mn_num] = turn + 2
        scores[mn_num] += C
        santa_move(mn_num,si,sj,rdi,rdj,C)

    # [2] 산타의 움직임
    for idx in range(1,P+1):
        # 기절 혹은 사망
        if not is_live[idx]: continue
        if is_stun[idx] > turn: continue

        si, sj = santa[idx]
        alst = []
        mn_dist = (ri-si)**2 + (rj-sj)**2
        for di, dj in ((-1,0),(0,1),(1,0),(0,-1)):
            ni,nj = si+di,sj+dj
            dist = (ri-ni)**2 + (rj-nj)**2
            if 0<=ni<N and 0<=nj<N and mn_dist > dist and arr[ni][nj] <= 0:
                mn_dist = dist
                alst.append((ni,nj,di,dj))

        if not alst: continue


        # 산타 이동
        ni,nj,di,dj = alst[-1]

        # 산타 충돌
        if (ni,nj) == (ri,rj):
            is_stun[idx] = turn + 2
            scores[idx] += D
            arr[si][sj] = 0
            santa_move(idx,ni,nj,-di,-dj,D)

        else:
            arr[si][sj] = 0
            arr[ni][nj] = idx
            santa[idx] = [ni,nj]

    for i in range(1,P+1):
        if is_live[i]:
            scores[i] += 1

print(*scores[1:])