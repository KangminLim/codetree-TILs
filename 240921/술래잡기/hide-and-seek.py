N, M, H, K = map(int,input().split())
hider = {}
# 좌,우,하,상
di,dj = [0,0,1,-1],[-1,1,0,0]
opp = {0:1, 1:0, 2:3, 3:2}
arr = [[0] * N for _ in range(N)]
for idx in range(1,M+1):
    ci,cj,cd = map(int,input().split())
    hider[idx] = [ci-1,cj-1,cd]
tree = set()
for _ in range(H):
    ti,tj = map(int,input().split())
    tree.add((ti-1,tj-1))

tm = N//2
ti,tj,td = tm,tm,0
tdi,tdj = [-1,0,1,0], [0,1,0,-1]

ans = 0

mx_cnt, cnt, flag, val = 1,0,0,1


for turn in range(1,K+1):
    # 1. M명의 도망자 동시 이동
    for idx in hider:
        ci,cj,cd = hider[idx]
        # 1.1 거리 3 이하만
        if abs(ti-ci) + abs(tj-cj) > 3: continue

        ni,nj = ci+di[cd], cj+dj[cd]
        # 1.1.1 격자 안
        if 0<=ni<N and 0<=nj<N:
            if (ni,nj) != (ti,tj):
                hider[idx] = [ni,nj,cd]
        # 1.1.2 격자 밖
        else:
            cd = opp[cd]
            ni, nj = ci + di[cd], cj + dj[cd]
            if 0 <= ni < N and 0 <= nj < N:
                if (ni, nj) != (ti, tj):
                    hider[idx] = [ni, nj, cd]

    # 2. 술래 이동(달팽이 이동)
    arr[ti][tj] = turn # 디버깅 용
    ti,tj = ti+tdi[td], tj+tdj[td]
    cnt += 1

    if (ti,tj) == (0,0): # 원점 도착
        mx_cnt, cnt, flag, val = N, 1, 1, -1
        td = 2
    elif (ti,tj) == (tm,tm):
        mx_cnt, cnt, flag, val = 1, 0, 0, 1
        td = 0
    else:
        if mx_cnt == cnt:
            cnt = 0
            td = (td+val)%4
            if flag:
                mx_cnt += val
                flag = 0
            else:
                flag = 1

    # 3. 술래 잡기
    tset = set(((ti,tj),(ti+tdi[td],tj+tdj[td]),(ti+tdi[td]*2,tj+tdj[td]*2)))
    for idx in range(1,M+1):
        if idx not in hider: continue
        hi,hj,_ = hider[idx]
        if (hi,hj) not in tree and (hi,hj) in tset:
            ans += turn
            hider.pop(idx)
print(ans)