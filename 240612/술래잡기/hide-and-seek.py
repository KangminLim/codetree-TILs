N,M,H,K = map(int,input().split())
arr = [[0] * N for _ in range(N)]
hider = {}
di,dj = [0,0,1,-1], [-1,1,0,0]
opp = {0:1,1:0,2:3,3:2}
tm = N//2
ans = 0
ti,tj,tdr = tm, tm, 0
tdi,tdj = [-1,0,1,0], [0,1,0,-1]
mx_cnt, cnt, flag, val = 1, 0, 0, 1

for idx in range(1,M+1):
    i,j,dr = map(int,input().split())
    hider[idx] = [i-1,j-1,dr]

tree = set()

for _ in range(H):
    i,j = map(int,input().split())
    tree.add((i-1,j-1))

for turn in range(1,K+1):
    # 술래 동시에 이동
    for idx in hider:
        ci,cj,cd = hider[idx]
        dist = abs(ti-ci) + abs(tj-cj)
        if dist > 3: continue # 거리 3 이상 차이면 움직이지 않음

        ni, nj = ci+di[cd], cj+dj[cd]
        if 0<=ni<N and 0<=nj<N: # 범위 내
            if (ni,nj) == (ti,tj): continue
            else:
                hider[idx] = [ni,nj,cd]
        else: # 범위 밖
            nd = opp[cd]
            ni, nj = ci + di[nd], cj + dj[nd]
            if (ni,nj) == (ti,tj):
                hider[idx] = [ci,cj,nd]
            else:
                hider[idx] = [ni,nj,nd]

    arr[ti][tj] = turn  # 디버깅용
    ti,tj = ti+tdi[tdr], tj+tdj[tdr]
    cnt += 1
    # 1,1 2,2, 3,3, 4,4 5,5 : 달팽이 이동
    if (ti,tj) == (0,0):
        mx_cnt, cnt, flag, val = N, 1, 1, -1
        tdr = 2
    elif (ti,tj) == (tm,tm):
        mx_cnt, cnt, flag, val = 1, 0, 0, 1
        tdr = 0
    else:
        if mx_cnt == cnt:
            # mx_cnt와 cnt 같아지면 방향 변경
            tdr = (tdr + val) % 4
            cnt = 0
            if flag: # 2번마다 길이 증가
                flag = 0
                mx_cnt += val
            else: # 한번 더 진행
                flag = 1


    for i in range(1,M+1):
        if i in hider:
            ci,cj,_ = hider[i]
            if (ci,cj) not in ((ti,tj),(ti+tdi[tdr],tj+tdj[tdr]),(ti+2*tdi[tdr],tj+2*tdj[tdr])) or (ci,cj) in tree: continue
            else:
                ans += turn
                hider.pop(i)

print(ans)