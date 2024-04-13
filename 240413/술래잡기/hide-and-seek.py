N,M,H,K = map(int,input().split())
arr = [[0] * (N+2) for _ in range(N+2)]
hider = {}
di,dj = [0,0,1,-1], [-1,1,0,0]
opp = {0:1, 1:0, 2:3, 3:2}
is_live = [True] * (M+1)
is_live[0] = False
for m in range(1,M+1):
    i,j,dr = map(int,input().split())
    hider[m] = [i,j,dr]
    arr[i][j] = m
ans = 0
tree = set()
for _ in range(H):
    i,j = map(int,input().split())
    tree.add((i,j))

tdi,tdj = [-1,0,1,0], [0,1,0,-1]
tm = (N+1)//2
ti,tj,td = tm,tm,0
mx_cnt, cnt, flag, val = 1,0,0,1


for t in range(1,K+1):
    for idx in range(1,M+1):
        if not is_live[idx] : continue
        ci,cj,cd = hider[idx]
        if abs(ti-ci)+abs(tj-cj) <= 3:
            ni,nj = ci+di[cd], cj+dj[cd]
            if 1<=ni<=N and 1<=nj<=N:
                if (ni,nj) != (ti,tj):
                    hider[idx] = [ni,nj,cd]
            else:
                nd = opp[cd]
                if (ni,nj) != (ti,tj):
                    hider[idx] = [ni,nj,nd]

    cnt += 1
    ti,tj = ti+tdi[td], tj+tdj[td]

    if (ti,tj) == (1,1):
        mx_cnt, cnt, flag, val = N,1,1,-1
        td =2
    elif (ti,tj) == (tm,tm):
        mx_cnt, cnt, flag, val = 1, 0, 0, 1
        td = 0
    else:
        if mx_cnt == cnt:
            cnt = 0
            td = (td+val)%4

            if flag == 0:
                flag = 1
            else:
                flag = 0
                mx_cnt += val

    pset = set(((ti,tj),(ti+tdi[td],tj+tdj[td]),(ti+tdi[td]*2,tj+tdj[td]*2)))

    for idx in range(1,M+1):
        if not is_live[idx]: continue
        ci,cj,_ = hider[idx]
        if (ci,cj) in pset and (ci,cj) not in tree:
            is_live[idx] = False
            ans += t

print(ans)