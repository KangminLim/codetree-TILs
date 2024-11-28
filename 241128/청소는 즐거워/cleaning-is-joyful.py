N = int(input())
arr = [list(map(int,input().split())) for _ in range(N)]
# narr = [[0] * N for _ in range(N)] 달팽이 이동 디버깅용
ti,tj, td = N//2, N//2, 0
tdi, tdj = [0,1,0,-1], [-1,0,1,0]
nlst = [2, 10, 7, 1, 5, 10, 7, 1, 2]
mx_cnt, cnt, flag = 1,0,0
# num = 0
ans = 0
while (ti,tj) != (0,0):
    # num += 1
    # 1. 달팽이 이동
    ti,tj = ti+tdi[td],tj+tdj[td]
    cnt += 1

    cur = arr[ti][tj]
    arr[ti][tj] = 0
    a = 0
    if td == 0:
        slst = [(-2,0),(-1,-1),(-1,0),(-1,1),(0,-2),(1,-1),(1,0),(1,1),(2,0)]
        for i in range(len(slst)):
            di,dj = slst[i]
            ni,nj = ti+di, tj+dj
            a += int(cur*0.01*nlst[i])
            if 0<=ni<N and 0<=nj<N:
                arr[ni][nj] += int(cur*0.01*nlst[i])
            else:
                ans += int(cur*0.01*nlst[i])
        ni,nj = ti,tj-1
        if 0 <= ni < N and 0 <= nj < N:
            arr[ni][nj] += (cur-a)
        else:
            ans += (cur-a)

    elif td == 1:
        slst = [(0,-2),(1,-1),(0,-1),(-1,-1),(2,0),(1,1),(0,1),(-1,1),(0,2)]
        for i in range(len(slst)):
            di, dj = slst[i]
            ni, nj = ti + di, tj + dj
            a += int(cur*0.01*nlst[i])
            if 0 <= ni < N and 0 <= nj < N:
                arr[ni][nj] += int(cur*0.01*nlst[i])
            else:
                ans += int(cur*0.01*nlst[i])
        ni, nj = ti+1,tj
        if 0 <= ni < N and 0 <= nj < N:
            arr[ni][nj] += (cur-a)
        else:
            ans += (cur-a)
    elif td == 2:
        slst = [(-2,0),(-1,1),(-1,0),(-1,-1),(0,2),(1,1),(1,0),(1,-1),(2,0)]
        for i in range(len(slst)):
            di, dj = slst[i]
            ni, nj = ti + di, tj + dj
            a += int(cur*0.01*nlst[i])
            if 0 <= ni < N and 0 <= nj < N:
                arr[ni][nj] += int(cur*0.01*nlst[i])
            else:
                ans += int(cur*0.01*nlst[i])
        ni, nj = ti,tj+1
        if 0 <= ni < N and 0 <= nj < N:
            arr[ni][nj] += (cur-a)
        else:
            ans += (cur-a)
    elif td == 3:
        slst = [(0,2),(-1,1),(0,1),(1,1),(-2,0),(-1,-1),(0,-1),(1,-1),(0,-2)]
        for i in range(len(slst)):
            di, dj = slst[i]
            ni, nj = ti + di, tj + dj
            a += int(cur*0.01*nlst[i])
            if 0 <= ni < N and 0 <= nj < N:
                arr[ni][nj] += int(cur*0.01*nlst[i])
            else:
                ans += int(cur*0.01*nlst[i])
        ni, nj = ti-1, tj
        if 0 <= ni < N and 0 <= nj < N:
            arr[ni][nj] += (cur-a)
        else:
            ans += (cur-a)
    # print('')

    # narr[ti][tj] = num 달팽이 이동 디버깅용
    if mx_cnt == cnt:
        cnt = 0
        td = (td + 1) % 4
        if flag:
            mx_cnt += 1
            flag = False
        else:
            flag = True
    # print('')
print(ans)