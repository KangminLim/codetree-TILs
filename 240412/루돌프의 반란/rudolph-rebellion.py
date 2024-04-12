N, M, P, C, D = map(int,input().split())
arr = [[0] * N for _ in range(N)]
ri,rj = map(lambda x:int(x)-1, input().split())
arr[ri][rj] = -1

santa = {}
for _ in range(1,P+1):
    idx, i, j = map(int,input().split())
    santa[idx] = [i-1,j-1]
    arr[i-1][j-1] = idx

is_live = [True] * (P+1)
is_live[0] = False
is_stun = [0] * (P+1)
scores = [0] * (P+1)

from collections import deque
def santa_move(cur,ci,cj,di,dj,mul):
    q = deque()
    q.append((cur,ci,cj,mul))
    while q:
        cur,ci,cj,mul = q.popleft()

        ni,nj = ci+di*mul, cj+dj*mul

        if 0<=ni<N and 0<=nj<N: # 범위 내
            if arr[ni][nj] == 0: # 빈 칸
                arr[ni][nj] = cur
                santa[cur] = [ni,nj]
                return
            else:
                q.append((arr[ni][nj],ni,nj,1))
                arr[ni][nj] = cur
                santa[cur] = [ni, nj]

        else: # 범위 밖
            is_live[cur] = False
            return

# M턴동안 진행
for turn in range(1,M+1):
    # 모든 산타가 탈락했으면 break
    if is_live.count(True) == 0: break
    min_dist = 2*N**2
    # [1] 루돌프 이동
    # [1-1] 가장 가까운 산타 지정하기
    for idx in range(1,P+1):
        if not is_live[idx] : continue
        si,sj = santa[idx]
        dist = (ri-si)**2 + (rj-sj)**2
        if min_dist > dist: # 원래 거리보다 가까워지는 산타가 생기면
            min_dist = dist
            tlst = [(si,sj,idx)]
        elif min_dist==dist : # 2명 이상
            tlst.append((si,sj,idx))

    if len(tlst) >= 2: # 가까워지는 산타가 2명 이상일 경우
        tlst.sort(reverse=True) #행, 열이 큰 순으로 정렬

    si,sj,mn_idx = tlst[0] # 가장 가까운 산타 지정

    # [1-2] 8방향 이동
    rdi,rdj = 0, 0

    if ri > si: rdi = -1
    elif ri < si : rdi = 1

    if rj > sj : rdj = -1
    elif rj < sj : rdj = 1

    arr[ri][rj] = 0 # 위치 업데이트
    ri,rj = ri+rdi, rj+rdj
    arr[ri][rj] = -1 # 위치 업데이트

    # [1-3] 루돌프 충돌
    if (ri,rj) == (si,sj):
        scores[mn_idx] += C
        is_stun[mn_idx] = turn + 2
        santa_move(mn_idx,si,sj,rdi,rdj,C)

    # [2] 산타 이동

    # [2-1] 1~P 순서대로 이동
    for idx in range(1,P+1):
        # 기절 혹은 사망하면 continue
        if not is_live[idx] : continue
        if is_stun[idx] > turn : continue

        si,sj = santa[idx]
        min_dist = (ri-si)**2 + (rj-sj)**2
        alst = []
        for di,dj in ((-1,0),(0,1),(1,0),(0,-1)):
            ni,nj = si+di,sj+dj
            dist = (ri-ni)**2 + (rj-nj)**2
            if 0<=ni<N and 0<=nj<N and arr[ni][nj]<=0 and min_dist > dist:
                min_dist = dist
                alst.append((ni,nj,di,dj)) # 다음위치 및 di,dj 저장
        if not alst: continue # 가까워지는 방법이 없음

        ni,nj,di,dj = alst[-1] # 가장 마지막에 쌓인게 가장 가까운
        arr[si][sj] = 0

        if (ni,nj) == (ri,rj): # 산타 충돌
            is_stun[idx] = turn + 2
            scores[idx] += D
            santa_move(idx,ni,nj,-di,-dj,D)

        else: # 빈 칸
            arr[ni][nj] = idx
            santa[idx] = [ni,nj]

    for idx in range(1,P+1):
        if is_live[idx]:
            scores[idx] += 1

print(*scores[1:])