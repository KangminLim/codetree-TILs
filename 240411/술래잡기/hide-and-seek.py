N, M, H, K = map(int,input().split())

arr = [[0] * (N+2) for _ in range(N+2)]

hider = {}

for idx in range(1,M+1):
    x,y,dir = map(int,input().split())
    hider[idx] = [x,y,dir]

is_live = [True] * (M+1)
is_live[0] = False

tree = set()
for _ in range(H):
    i,j = map(int,input().split())
    tree.add((i,j))


di,dj = [0,0,1,-1], [-1,1,0,0]
opp = {0:1,1:0,2:3,3:2}

tm = (N+1)//2
ti,tj,td = tm,tm,0
tdi,tdj = [-1,0,1,0], [0,1,0,-1]

mx_cnt, cnt, flag, val = 1,0,0,1
ans = 0

for turn in range(1,K+1):
    # 도망자 이동
    for idx in hider:
        if not is_live : continue
        ci,cj,cd = hider[idx]
        if abs(ci-ti) + abs(cj-tj) <= 3:
            ni,nj = ci+di[cd], cj+dj[cd]
            if 1<=ni<=N and 1<=nj<=N:
                if (ni,nj) != (ti,tj):
                    hider[idx] = [ni,nj,cd]
            else:
                nd = opp[cd]
                ni,nj = ci+di[nd], cj+dj[nd]
                if (ni,nj) != (ti,tj):
                    hider[idx] = [ni,nj,nd]
    # 술래 이동
    cnt += 1
    # arr[ti][tj] = turn
    ti,tj = ti+tdi[td], tj+tdj[td]

    if (ti,tj) == (1,1):
        mx_cnt, cnt, flag, val = 5, 1, 1, -1
        td = 2
    elif (ti,tj) == (tm,tm):
        mx_cnt, cnt, flag, val = 1, 0, 0, 1
        td = 0
    else:
        if mx_cnt == cnt:
            cnt = 0
            td = (td+val)%4

            if flag == 1:
                flag = 0
                mx_cnt += val
            else:
                flag = 1

    # 술래 잡기
    pset = set(((ti,tj),(ti+di[td],tj+dj[td]),(ti+di[td]*2,tj+dj[td]*2)))

    for idx in hider:
        if not is_live[idx] : continue
        ci,cj,_ = hider[idx]
        if (ci,cj) in pset and (ci,cj) not in tree:
            ans += turn
            is_live[idx] = False


print(ans)