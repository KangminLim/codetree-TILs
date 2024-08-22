arr = [[0] * 4 for _ in range(4)]
# 몬스터 마리 수, 턴의 수
M, T = map(int,input().split())
# 팩맨 초기 위치
pi,pj = map(lambda x:int(x)-1,input().split())
# arr[pi][pj] = -1
# 몬스터 정보
mlst = []
for i in range(M):
    ci, cj, cd = map(int,input().split())
    mlst.append((ci-1,cj-1,cd-1))
    arr[ci-1][cj-1] += 1
# 몬스터 시체 처리
is_live = [[0] * 4 for _ in range(4)]
di, dj = [-1,0,1,0], [0,-1,0,1]
mdi, mdj = [-1,-1,0,1,1,1,0,-1], [0,-1,-1,-1,0,1,1,1]
for turn in range(1,T+1):
    tlst = []
    # 1. 몬스터 복제 시도
    for ci,cj,cd in mlst:
        tlst.append((ci,cj,cd))
    # 2. 몬스터 이동
    for i in range(len(mlst)):
        ci,cj,cd = mlst[i]
        for k in range(8):
            ni,nj = ci+mdi[(cd+k)%8], cj+mdj[(cd+k)%8]
            # 몬스터 시체가 있거나, 팩맨이 있거나, 격자를 벗어나는 경우는 continue
            if not (0<=ni<4 and 0<=nj<4) or turn <= is_live[ni][nj] or (ni,nj) == (pi,pj):
                continue
            else:
                mlst[i] = [ni,nj,(cd+k)%8]
                arr[ci][cj] -= 1
                arr[ni][nj] += 1
                break
    # 3. 팩맨 이동
    # 3.1 3단 이동
    mx = 0
    fi,fj,si,sj = 5,5,5,5
    mpi,mpj = pi, pj
    # arr[pi][pj] = 0
    for i in range(4):
        t1pi, t1pj = pi + di[i], pj + dj[i]
        if 0 <= t1pi < 4 and 0 <= t1pj < 4:
            first_score = arr[t1pi][t1pj]
            for j in range(4):
                t2pi, t2pj = t1pi + di[j], t1pj + dj[j]
                if 0<=t2pi<4 and 0<=t2pj<4:
                    if (t2pi,t2pj) != (t1pi,t1pj):
                        second_score = arr[t2pi][t2pj]
                    else:
                        second_score = 0
                    for k in range(4):
                        t3pi, t3pj = t2pi + di[k], t2pj + dj[k]
                        if 0<=t3pi<4 and 0<=t3pj<4:
                            if (t3pi,t3pj) != (t2pi,t2pj):
                                third_score = arr[t3pi][t3pj]
                            else:
                                third_score = 0
                            cnt = first_score + second_score + third_score
                            if cnt > mx:
                                mx = max(cnt,mx)
                                fi,fj,si,sj = t1pi,t1pj,t2pi, t2pj
                                mpi, mpj = t3pi, t3pj
    pi, pj = mpi, mpj
    if arr[fi][fj] > 0:
        is_live[fi][fj] = turn + 2
    if arr[si][sj] > 0:
        is_live[si][sj] = turn + 2
    if arr[pi][pj] > 0:
        is_live[pi][pj] = turn + 2
    arr[fi][fj] = 0
    arr[si][sj] = 0
    arr[pi][pj] = 0

    tmlst = []
    # 죽은 몬스터 처리
    for i in range(len(mlst)):
        mi,mj,md = mlst[i]
        if (mi,mj) != (fi,fj) and (mi,mj) != (si,sj) and (mi,mj) != (pi,pj):
            tmlst.append((mi,mj,md))

    for ti, tj, td in tlst:
        arr[ti][tj] += 1
        tmlst.append((ti,tj,td))

    mlst = tmlst

ans = 0
for lst in arr:
    for i in range(4):
        if lst[i] > 0:
            ans += lst[i]
print(ans)