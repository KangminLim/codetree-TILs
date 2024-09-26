N, M, H, K = map(int,input().split())
hider = {}
arr = [[0] * N for _ in range(N)]
di,dj = [0,0,1,-1],[-1,1,0,0]
opp = {0:1,1:0,2:3,3:2}
for idx in range(1,M+1):
    hi, hj, hd = map(int,input().split())
    hider[idx] = [hi-1,hj-1,hd]

tree = set()
for _ in range(H):
    ti,tj = map(lambda x:int(x)-1, input().split())
    tree.add((ti,tj))

TM = N//2
ti,tj,td = TM,TM,0
tdi,tdj = [-1,0,1,0],[0,1,0,-1]
mx_cnt,cnt,flag,val = 1,0,0,1
ans = 0
for turn in range(1,K+1):
    # 1.도망자 이동
    for idx in hider:
        hi,hj,hd = hider[idx]
        if abs(hi-ti) + abs(hj-tj) > 3: continue
        ni,nj = hi+di[hd], hj+dj[hd]

        # 격자 안
        if 0<=ni<N and 0<=nj<N:
            # 술래 없으면
            if (ni,nj) != (ti,tj):
                hider[idx] = [ni,nj,hd]
                arr[hi][hj] = 0
                arr[ni][nj] = idx

        else:
            hd = opp[hd]
            ni, nj = hi + di[hd], hj + dj[hd]
            if (ni,nj) != (ti,tj):
                hider[idx] = [ni,nj,hd]
                arr[hi][hj] = 0
                arr[ni][nj] = idx

            else:
                hider[idx] = [hi,hj,hd]
    # 2.술래 이동
    # arr[ti][tj] = turn # 디버깅용
    ti,tj = ti+tdi[td], tj+tdj[td]
    cnt += 1
    if (ti,tj) == (0,0):
        mx_cnt, cnt, flag, val = N, 1, 1, -1
        td = 2
    elif (ti,tj) == (TM,TM):
        mx_cnt, cnt, flag, val = 1, 0, 0, 1
        td = 0
    else:
        if mx_cnt == cnt:
            cnt = 0
            td = (td+val)%4
            if flag:
                mx_cnt += val
                flag = False
            else:
                flag = True

    # 3. 술래 잡기

    tset = set(((ti,tj),(ti+tdi[td],tj+tdj[td]),(ti+tdi[td]*2,tj+tdj[td]*2)))
    for idx in range(1,M+1):
        if idx in hider:
            hi,hj,hd = hider[idx]
            if (hi,hj) in tset and (hi,hj) not in tree:
                ans += turn
                arr[hi][hj] = 0
                hider.pop(idx)

print(ans)