N, M, P, C, D = map(int,input().split())
mp = [[0] * N for _ in range(N)]
# 루돌프 입력
ri, rj = map(lambda x: int(x)-1, input().split())
mp[ri][rj] = -1
# 산타 입력
santa = [[N] * 2 for _ in range(P+1)]
for _ in range(P):
    n, i, j = map(int,input().split())
    santa[n] = [i-1,j-1]
    mp[i-1][j-1] = n
is_stun = [1] * (P+1)
is_live = [True] * (P+1)
is_live[0] = False
scores = [0] * (P+1)

def santa_move(cur,si,sj,di,dj,mul):

    q = [(cur,si,sj,mul)]

    while q:
        cur, si, sj, mul = q.pop(0)
        ni, nj = si + di * mul, sj + dj * mul
        if 0<=ni<N and 0<=nj<N: # 게임판 안
           if mp[ni][nj] > 0: # 산타가 있다면
               q.append((mp[ni][nj],ni,nj,1)) # 1칸 씩 연쇄 이동
               mp[ni][nj] = cur
               santa[cur] = [ni,nj]
           else:
               mp[ni][nj] = cur
               santa[cur] = [ni,nj]
               return

        else: # 게임판 밖으로 밀려나오면 탈락
            is_live[cur] = False
            return

for turn in range(1,M+1):
    # 모두 죽었으면 break
    if is_live.count(True)==0: break

    # [1] 루돌프의 움직임
    # [1-1] 가장 가까운 산타 1명 고르기
    mindist = 2*N**2
    for idx in range(1,P+1):
        if not is_live[idx] : continue # 죽은 산타는 돌격당하지 않음
        si, sj = santa[idx]
        dist = (ri-si)**2 + (rj-sj)**2
        if mindist > dist:
            mindist = dist
            mlst = [(si,sj,idx)] # 돌격당하는 산타의 i,j,idx 저장
        elif mindist == dist: # 산타가 2명 이상이면
            mlst.append((si,sj,idx))
    mlst.sort(reverse=True)
    si,sj,mn_num = mlst[0] # 돌격 당하는 산타 지정

    # [1-2] 8방향 지정
    rdi, rdj = 0, 0
    # 행이 더 클 경우 행을 줄인다
    if ri > si : rdi = -1
    elif ri < si : rdi = 1

    # 열이 더 클 경우 열을 줄인다
    if rj > sj  : rdj = -1
    elif rj < sj : rdj = 1

    # 루돌프 이동 처리
    mp[ri][rj] = 0
    ri, rj = ri+rdi, rj+rdj
    mp[ri][rj] = -1

    # [1-3] 루돌프의 충돌
    if (ri,rj) == (si,sj):
        scores[mn_num] += C
        is_stun[mn_num] = turn + 2
        santa_move(mn_num,si,sj,rdi,rdj,C) # 산타는 루돌픋가 이동해온 방향으로 C칸 만큼 밀려나게 된다.

    # [2] 산타의 움직임
    for idx in range(1,P+1):
        # 기절 혹은 사망한 산타는 움직일 수 없다
        if not is_live[idx] or is_stun[idx] > turn : continue

        # [2-1] 각 산타에서 루돌프와 가장 가까운 거리 구하기
        si,sj = santa[idx]
        mn_dist = (ri-si)**2 + (rj-sj)**2
        tlst = []
        # 상,우,하,좌 우선순위로 이동 / 가까워질 수 있으면 이동 x / 다른 산타가 있는 칸이나, 게임판 밖으로는 움직일 수 없음
        for di, dj in ((-1,0),(0,1),(1,0),(0,-1)):
            ni, nj = si+di, sj+dj
            dist = (ri-ni)**2 + (rj-nj)**2
            if 0<=ni<N and 0<=nj<N and mp[ni][nj] <=0 and mn_dist > dist:
                mn_dist = dist
                tlst.append((ni,nj,di,dj)) # 이동해온 방향도 알아야 하므로 ni,nj,di,dj로 저장
        if not tlst: continue # tlst가 비었다 => 가까워질 수 있는 거리가 없다 continue
        ni,nj,di,dj = tlst[-1] # 제일 마지막에 쌓인게 가장 짧은 거리

        # [2-2] 산타 충돌
        if (ni,nj) == (ri,rj):
            scores[idx] += D
            is_stun[idx] = turn + 2
            mp[si][sj] = 0
            santa_move(idx,ni,nj,-di,-dj,D) #반대 방향으로 D만큼 밀려남
        else: # 빈칸일 경우
            mp[si][sj] = 0
            santa[idx] = [ni,nj]
            mp[ni][nj] = idx

    for idx in range(1,P+1):
        if is_live[idx]:
            scores[idx] += 1

print(*scores[1:])