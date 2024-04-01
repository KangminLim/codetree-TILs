N, M, P, C, D = map(int,input().split())

mp = [[0] * N for _ in range(N)]

Rr,Rc = map(lambda x:int(x)-1, input().split())
mp[Rr][Rc] = -1 # 루돌프 위치
is_live = [1] * (P+1)
is_live[0] = 0
is_stun = [1] * (P+1)
scores = [0] * (P+1)
# 산타 위치
santa = [[N]*2 for _ in range(P+1)]

for _ in range(1,P+1):
    idx, r,c = map(int,input().split())
    santa[idx] = [r-1,c-1]
    mp[r-1][c-1] = idx

def move_santa(cur,ci,cj,di,dj,mul):

    q = [(cur,ci,cj,mul)]

    while q:
        cur, ci, cj, mul = q.pop(0)
        ni, nj = ci + di*mul, cj+ dj*mul
        if 0<=ni<N and 0<=nj<N:
            if mp[ni][nj] == 0:
                mp[ni][nj] = cur
                santa[cur] = [ni,nj]
                return
            else:
                q.append((mp[ni][nj],ni,nj,1))
                mp[ni][nj] = cur
                santa[cur] = [ni,nj]
        else:
            is_live[cur] = 0
            return

for turn in range(1,M+1):

    if is_live.count(1) == 0:
        break
    # [1] 루돌프의 움직임
    # [1-1] 가장 가까운 산타 고르기
    # 탈락한 산타는 지정 못당함

    mdist = 2 * N ** 2
    for idx in range(1,P+1):
        if is_live[idx] == 0 : continue
        Sr, Sc = santa[idx]
        dis = (Rr-Sr)**2 + (Rc-Sc)**2
        if mdist > dis:
            mdist = dis
            mlst = [(Sr,Sc,idx)]
        elif mdist == dis:
            mlst.append((Sr,Sc,idx))

    mlst.sort(reverse=True) # R좌표 우선 정렬
    Si, Sj, mn_idx = mlst[0] # 돌격 목표 산타
    Rdi, Rdj = 0, 0
    # 행이 크면 행을 줄임
    if Rr > Si: Rdi = -1
    elif Rr < Si : Rdi = 1

    # 열이 크면 열을 줄임
    if Rc > Sj : Rdj = -1
    elif Rc < Sj : Rdj = 1

    mp[Rr][Rc] = 0 # 루돌프 이동 처리
    Rr, Rc = Rr + Rdi, Rc + Rdj
    mp[Rr][Rc] = -1

    # [1-2] 루돌프의 충돌
    if (Rr,Rc) == (Si,Sj):
        scores[mn_idx] += C
        is_stun[mn_idx] = turn + 2
        move_santa(mn_idx,Si,Sj,Rdi,Rdj,C)



    # [2] 산타의 움직임
    for idx in range(1,P+1):
        if is_live[idx] == 0 : continue
        if is_stun[idx] > turn : continue
        ci,cj = santa[idx]
        tlst = []
        minDist = (Rr-ci)**2 + (Rc-cj)**2
        for di,dj in ((-1,0),(0,1),(1,0),(0,-1)):
            ni, nj =  ci + di, cj + dj
            Dist = (Rr - ni) ** 2 + (Rc - nj) ** 2
            if 0<=ni<N and 0<=nj<N and mp[ni][nj] <= 0 and minDist > Dist:# 빈칸이고, 범위 벗어나지 않으면 이동 가능
                minDist = Dist
                tlst.append((ni,nj,di,dj))
        if len(tlst) == 0: continue
        ni,nj,di,dj = tlst[-1]

        if (Rr,Rc) == (ni,nj): # 루돌프와 충돌 : 반대로 이동
            scores[idx] += D
            is_stun[idx] = turn+2
            mp[ci][cj] = 0
            move_santa(idx,ni,nj,-di,-dj,D)
        else:
            mp[ci][cj] = 0
            mp[ni][nj] = idx
            santa[idx] = [ni,nj]

    for i in range(1,P+1):
        if is_live[i] == 1:
            scores[i] += 1

print(*scores[1:])