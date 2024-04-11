N, M, H, K = map(int,input().split())
hider = {}
for m in range(1,M+1):
    i,j,dr = map(int,input().split())
    hider[m] = [i,j,dr]
is_live = [True] * (M+1)
is_live[0] = False
di,dj = [0,0,1,-1], [-1,1,0,0]
opp = {0:1, 1:0, 2:3, 3:2}
narr= [[0]*(N+2) for _ in range(N+2)]
tree = set()
for _ in range(H):
    i,j = map(int,input().split())
    tree.add((i,j))

tm = (N+1)//2
ti,tj,td = tm,tm,0
tdi,tdj = [-1,0,1,0],[0,1,0,-1]
mx_cnt,cnt, flag, val = 1,0,0,1
ans = 0

for k in range(1,K+1):
    for idx in range(1,M+1):
        if not is_live[idx] : continue
        ci,cj,cd = hider[idx]
        if abs(ti-ci) + abs(tj-cj) <= 3:
            ni,nj = ci+di[cd], cj+dj[cd]
            if not (1<=ni<=N and 1<=nj<=N): #격자를 벗어남
                nd = opp[cd]
                ni,nj = ci+di[nd], cj+dj[nd]
                if (ni,nj) != (ti,tj):
                    hider[idx] = [ni,nj,nd]
            else: # 격자 안
                if (ni,nj) != (ti,tj):
                    hider[idx] = [ni,nj,cd]

    #  술래 이동
    cnt += 1
    narr[ti][tj] = k
    ti,tj = ti+tdi[td], tj + tdj[td]

    if (ti,tj) == (1,1):
        mx_cnt, cnt, flag, val = N, 1, 1, -1
        td = 2
    elif (ti,tj) == (tm,tm):
        mx_cnt, cnt, flag, val = 1, 0, 0, 1
        td = 0
    else:
        if mx_cnt == cnt:
            cnt = 0
            td = (td+val)%4

            if flag == 0:
                flag =1
            else:
                flag = 0
                mx_cnt += val

    pset = set(((ti,tj),(ti+tdi[td],tj+tdj[td]),(ti+tdi[td]*2,tj+tdj[td]*2)))

    for idx in hider:
        if not is_live[idx]: continue

        ci,cj,_ = hider[idx]
        if (ci,cj) in pset and (ci,cj) not in tree:
            ans += k
            is_live[idx] = False

print(ans)