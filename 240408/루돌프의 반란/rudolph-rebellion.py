N, M, P, C, D = map(int,input().split())
ri, rj = map(lambda x:int(x)-1,input().split())
arr = [[0] * N for _ in range(N)]
arr[ri][rj] = -1 # 루돌프 위치
santa = [[N]*2 for _ in range(N+1)]

for _ in range(P):
    idx, i, j = map(int,input().split())
    santa[idx] = [i-1,j-1]
    arr[i-1][j-1] = idx

is_live = [True] * (P+1)
is_live[0] = False
is_stun = [1] * (P+1)
scores = [0] * (P+1)

from collections import deque
def santa_move(num,si,sj,di,dj,mul):
    q = deque()
    q.append((num,si,sj,mul))

    while q:
        cur, si, sj, mul = q.popleft()
        ni,nj = si+di*mul, sj+dj*mul
        if 0<=ni<N and 0<=nj<N: # 범위 내
            if arr[ni][nj]>0: # 산타를 만나면
                q.append((arr[ni][nj],ni,nj,1))
                arr[ni][nj] = cur
                santa[cur] = [ni,nj]
            else:
                arr[ni][nj] = cur #이동 처리
                santa[cur] = [ni,nj] #이동 처리
                return
        else: # 범위 밖
            is_live[cur] = False
            return
# 게임 시작
for turn in range(1,M+1):
    if is_live.count(True) == 0:  break # 다 탈락이면 종료
    min_dist = 100 ** 2
    # [1] 루돌프의 움직임
    # [1-1] 가까운 산타 선정
    for idx in range(1,P+1):
        if not is_live[idx]: continue # 탈락이면 선정 X
        si,sj = santa[idx]
        dist = (ri-si)**2 + (rj-sj)**2
        if min_dist > dist: # 가장 가까운 산타(1명)
            min_dist = dist
            tlst = [[si,sj,idx]]
        elif min_dist == dist: #가장 가까운 산타(2명 이상)
            tlst.append([si,sj,idx])

    # [1-2] 가장 가까운 산타 선택 완료 / r좌표 큰, c좌표 큰
    if tlst:
        tlst.sort(reverse=True)
    si,sj,mn_idx = tlst[0]

    # [1-3] 8방향 이동
    rdi, rdj = 0,0
    if ri > si : rdi = -1 # 행이 크면 줄이기
    elif ri < si : rdi = 1

    if rj > sj : rdj = -1
    elif rj < sj : rdj = 1

    arr[ri][rj] = 0 # 루돌프 이동 처리
    ri,rj = ri+rdi, rj+rdj
    arr[ri][rj] = -1

    # [1-4] 루돌프에 의한 충돌
    if (ri,rj) == (si,sj):
        is_stun[mn_idx] = turn + 2 # 2턴뒤에 정상화
        scores[mn_idx] += C
        santa_move(mn_idx,si,sj,rdi,rdj,C) # 루돌프 이동 방향대로 C만큼 이동

    # [2] 산타의 움직임
    # [2-1] 1~P 산타 순서대로 움직임
    for idx in range(1,P+1):
        if not is_live[idx]: continue
        if is_stun[idx] > turn : continue

        # [2-2] 루돌프와의 최단거리 찾기
        si, sj = santa[idx]
        min_dist = (ri-si)**2 + (rj-sj)**2
        slst = []
        for di,dj in ((-1,0),(0,1),(1,0),(0,-1)):
            ni, nj = si + di, sj + dj
            dist = (ri-ni)**2 + (rj-nj)**2
            if 0<=ni<N and 0<=nj<N and arr[ni][nj]<=0 and min_dist > dist: # 범위내, 산타가 있으면 안되고 최단거리 갱신
                min_dist = dist
                slst.append((ni,nj,di,dj))

        if not slst: continue # 움직이지 못하면 다음 산타

        ni,nj,di,dj = slst[-1] # 가장 마지막에 쌓인 slst가 최단거리

        # [2-3] 산타의 충돌

        if (ni,nj) == (ri,rj):
            is_stun[idx] = turn + 2
            scores[idx] += D
            arr[si][sj] = 0 # 이동처리
            santa_move(idx,ni,nj,-di,-dj,D) # 산타가 이동해온 반대 방향으로 D만큼 이동

        else:
            arr[si][sj] = 0
            arr[ni][nj] = idx
            santa[idx] = [ni,nj]


    # [3] 턴 종료
    for i in range(1,P+1):
        if is_live[i]:
            scores[i] += 1


print(*scores[1:])