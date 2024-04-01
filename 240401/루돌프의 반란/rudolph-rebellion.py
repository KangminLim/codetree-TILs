N, M, P, C, D = map(int,input().split())
mp = [[0] * N for _ in range(N)]

ri,rj = map(lambda x:int(x)-1, input().split())
mp[ri][rj] = -1 # 루돌프는 -1 표시

santa = [[N] * 2 for _ in range(P+1)]
is_live = [True] * (P+1)
is_live[0] = False
is_stun = [1] * (P+1)
scores = [0] * (P+1)


for _ in range(P):
    n, i, j = map(int,input().split())
    santa[n] = [i-1,j-1]
    mp[i-1][j-1] = n

def move_santa(cur,si,sj,di,dj,mul):
    q = []
    q.append((cur,si,sj,mul))
    while q:
        cur, si, sj, mul = q.pop(0)
        ni, nj = si+di*mul, sj+dj*mul

        if 0<=ni<N and 0<=nj<N: # 밀려난 위치가 범위 내
            if mp[ni][nj] == 0: # 빈칸이면 이동
                mp[ni][nj] = cur
                santa[cur] = [ni,nj]
                return
            else : # 산타가 있으면
                q.append((mp[ni][nj], ni, nj, 1))  # 1칸 이동
                mp[ni][nj] = cur
                santa[cur] = [ni,nj]

        else : # 범위 밖
            is_live[cur] = False
            return

for turn in range(1,M+1):
    # 모두 다 죽으면 게임 종료
    if is_live.count(True) == 0: break

    # [1] 루돌프 움직임
    # [1-1] 루돌프에게 가장 가까운 산타 정하기
    min_dist = 2*N**2
    for idx in range(1,P+1):
        if is_live[idx] == False: continue # 죽었으면

        si,sj = santa[idx]
        dist = (ri-si)**2 + (rj-sj)**2
        if dist < min_dist:
            min_dist = dist
            tlst = [(si,sj,idx)]
        elif dist == min_dist: # 가까운 산타가 2명 이상이라면
            tlst.append((si,sj,idx))
    tlst.sort(reverse=True) # r좌표가 큰 산타에게 가기 위해서 정렬 (i,j,idx)
    si, sj, mn_num = tlst[0] # 목표 산타의 i,j,idx
    
    # [1-2] 루돌프 이동 (8방향 이동)
    rdi,rdj = 0, 0
    # 루돌프 i가 더 크면 ri 줄이기
    if ri>si : rdi = -1
    elif ri<si: rdi = 1
    
    # 루돌프 j가 더 크면 rj 줄이기
    if rj>sj : rdj = -1
    elif rj<sj : rdj = 1
    
    # 루돌프 이동 반영
    mp[ri][rj] = 0
    ri, rj = ri + rdi, rj + rdj
    mp[ri][rj] = -1

    # [1-3] 루돌프의 충돌
    if (ri,rj) == (si,sj):
        scores[mn_num] += C # C점 획득
        is_stun[mn_num] = turn + 2 # K+2턴에 정상상태
        move_santa(mn_num,si,sj,rdi,rdj,C) # 산타의 밀려남 이동

    # [2] 산타의 움직임 (1~P 순서대로 이동)
    for idx in range(1,P+1):
        tlst = []
        if not is_live[idx] : continue
        if is_stun[idx] > turn: continue # 기절이거나 탈락한 산타는 움직일 수 없다
        si,sj = santa[idx]
        mn_dist = (ri-si)**2 + (rj-sj)**2 # 기존 산타와 루돌프의 거리
        for di,dj in ((-1,0),(0,1),(1,0),(0,-1)): # 상우하좌 우선순위
            ni, nj = si+di, sj+dj
            cur_dist = (ri-ni)**2 + (rj-nj)**2
            if 0<=ni<N and 0<=nj<N and mp[ni][nj] <= 0 and cur_dist < mn_dist:# 범위 내, 빈칸이고, 거리가 가까워 지면 이동
                mn_dist = cur_dist
                tlst.append((ni,nj,di,dj))
        if not tlst: continue # tlst가 빈리스트(최단거리가 없으면) 이동 X
        ci,cj,di,dj = tlst[-1] # 가장 늦은 리스트 원소가 가장 가까워지는 i,j

        # [2-1] 산타의 충돌
        if (ci,cj) == (ri,rj):
            scores[idx] += D
            is_stun[idx] = turn + 2
            mp[si][sj] = 0
            move_santa(idx,ci,cj,-di,-dj,D) # 산타의 밀려남 반대 이동
        else: #빈 칸이면 이동
            mp[si][sj] = 0
            mp[ci][cj] = idx
            santa[idx] = [ci,cj]

    for i in range(1,P+1):
        if is_live[i]:
            scores[i] += 1

print(*scores[1:])