N,M,H,K = map(int,input().split())
arr = [[0] * (N+2) for _ in range(N+2)]

hider = {}
for idx in range(1,M+1):
    i,j,dr = map(int,input().split())
    hider[idx] = [i,j,dr]

tree = set()

for _ in range(H):
    i,j = map(int,input().split())
    tree.add((i,j))

# 도망자 di,dj 좌우하상
di,dj = [0,0,1,-1], [-1,1,0,0]
opp = {0:1, 1:0, 2:3, 3:2}
is_live = [True] * (M+1)
is_live[0] = False

# 술래 tdi,tdj 상우하좌
tm = (N+1)//2
tdi,tdj = [-1,0,1,0], [0,1,0,-1]
ti,tj,td = tm,tm,0

# 달팽이 이동을 위한 변수
mx_cnt, cnt, flag, val = 1,0,0,1

ans = 0

# K턴 동안 진행
for k in range(1,K+1):
    # [1] 도망자의 이동
    for idx in hider:
        if not is_live[idx]: continue
        ci,cj,cd = hider[idx]
        # 거리 3이하 도망자만 이동
        if abs(ci-ti) + abs(cj-tj) <= 3:
            ni,nj = ci+di[cd], cj+dj[cd]
            if 1<=ni<=N and 1<=nj<=N: # 격자를 벗어나지 않는다면
                if (ni,nj) != (ti,tj): # 술래를 만나지 않는다면
                    hider[idx] = [ni,nj,cd]
            else: # 격자를 벗어나면 반대로 이동
                nd = opp[cd]
                ni,nj = ci+di[nd], cj+dj[nd]
                if (ni,nj) != (ti,tj):
                    hider[idx] = [ni,nj,nd]
    # [2] 술래의 이동
    cnt += 1
    arr[ti][tj] = k
    ti, tj = ti+tdi[td],tj+tdj[td]
    # [2-1] 좌상단 도착
    if (ti,tj) == (1,1):
        mx_cnt, cnt, flag, val = N, 1, 1, -1
        td = 2
    # [2-2] tm,tm 중앙 도착
    elif (ti,tj) == (tm,tm):
        mx_cnt, cnt, flag, val = 1, 0, 0, 1
        td = 0
    # [2-3] 2번에 한번 방향 및 mx_val 업데이트
    else:
        if mx_cnt == cnt:
            cnt = 0
            td = (td+val)%4

            if flag == 0:
                flag = 1
            else:
                flag = 0
                mx_cnt += val

    # [3] 범인 찾기
    # [3-1] 술래가 바라보고 있는 방향을 기준으로 본인 포함 3칸
    hset = set(((ti,tj),(ti+tdi[td],tj+tdj[td]),(ti+tdi[td]*2,tj+tdj[td]*2)))

    # [3-2] 도망자 탐색
    for idx in hider:
        if not is_live[idx] : continue
        ci,cj,_ = hider[idx]
        if (ci,cj) in hset and (ci,cj) not in tree:
            ans += k
            is_live[idx] = False

print(ans)