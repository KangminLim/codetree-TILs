N,M,H,K = map(int,input().split())
hider = {}
for idx in range(1,M+1):
    i,j,dr = map(int,input().split())
    hider[idx] = [i-1,j-1,dr]

arr = [[0] * N for _ in range(N)]
di,dj = [-1,0,1,0],[0,1,0,-1]
opp = {0:2, 1:3, 2:0, 3:1}

tree = set()
for _ in range(H):
    ti,tj = map(int,input().split())
    tree.add((ti-1,tj-1))

tM = N//2
ti,tj,td = tM,tM,0
tdi,tdj = [-1,0,1,0],[0,1,0,-1]

mx_cnt, cnt, flag, val = 1,0,0,1
ans = 0
for turn in range(1,K+1):

    for idx in range(1,M+1):
        # 1. 도망자 m명 이동
        if idx in hider:
            ci,cj,cd = hider[idx]
            dist = abs(ci-ti) + abs(cj-tj)
            if dist > 3: continue
            else:
                ni,nj = ci+di[cd], cj+dj[cd]
                if 0<=ni<N and 0<=nj<N: # 범위 내
                    if (ni,nj) != (ti,tj):
                        hider[idx] = [ni,nj,cd]
                else:
                    cd = opp[cd]
                    ni, nj = ci + di[cd], cj + dj[cd]
                    if (ni,nj) != (ti,tj):
                        hider[idx] = [ni,nj,cd]
                    else:
                        hider[idx] = [ci,cj,cd]

    arr[ti][tj] = turn
    ti,tj = ti+tdi[td], tj+tdj[td]
    cnt += 1

    if (ti,tj) == (0,0):
        mx_cnt, cnt, flag, val = N, 1, 1, -1
        td = 2

    elif (ti,tj) == (tM,tM):
        mx_cnt, cnt, flag, val = 1, 0, 0, 1
        td = 0

    else:
        if mx_cnt == cnt:
            td = (td+val)%4
            cnt = 0

            if flag == 0:
                flag = 1
            else:
                flag = 0
                mx_cnt += val

    tset = set(((ti,tj),(ti+tdi[td],tj+tdj[td]),(ti+2*tdi[td],tj+2*tdj[td])))

    for idx in range(1,M+1):
        if idx in hider:
            ci,cj,cd = hider[idx]
            if (ci,cj) in tset and (ci,cj) not in tree:
                ans += turn
                hider.pop(idx)

print(ans)