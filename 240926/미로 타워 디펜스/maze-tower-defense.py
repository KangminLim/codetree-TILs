N, M = map(int,input().split())
di, dj = [0,1,0,-1], [1,0,-1,0]
arr = [list(map(int,input().split())) for _ in range(N)]
ans = 0
tdi,tdj = [0,1,0,-1], [-1,0,1,0]
for turn in range(1,M+1):
    cd,mul = map(int,input().split())
    ci,cj = N//2, N//2
    for k in range(1,mul+1):
        ni,nj = ci+di[cd]*k, cj+dj[cd]*k
        ans += arr[ni][nj]
        arr[ni][nj] = 0
    # narr = [[0] * N for _ in range(N)]
    mx_cnt, cnt, flag, cd = 1, 0, 0, 0
    tlst = []
    for i in range(1,N*N):
        ci,cj = ci+tdi[cd],cj+tdj[cd]
        # narr[ci][cj] = i
        if arr[ci][cj] > 0:
            tlst.append(arr[ci][cj])
        cnt += 1
        if mx_cnt == cnt:
            cnt = 0
            cd = (cd+1)%4
            if flag:
                mx_cnt += 1
                flag = False
            else:
                flag = True

    # 3. tlst 순회하며 4개 이상이면 제거하고 붙이고 반복
    tlst.append(0) # while문을 위한 패딩
    while True:
        tmp = 0
        nlst = []
        while len(tlst)>1:
            cur = tlst.pop(0)
            cnt = 1
            i = 0
            while True:
                if cur == tlst[i]:
                    cnt += 1
                    i += 1
                else:
                    break
            if cnt < 4:
                for _ in range(cnt):
                    nlst.append(cur)
                if i >= 1:
                    for _ in range(i):
                        tlst.pop(0)
            else:
                tmp += cur * cnt
                for _ in range(i):
                    tlst.pop(0)
        tlst = nlst
        tlst.append(0)
        if tmp == 0:
            break
        else: ans += tmp

    # 4. 짝 짓기 (총 갯수, 숫자의 크기)
    nlst = []
    while len(tlst)>1:
        cur = tlst.pop(0)
        cnt = 1
        i = 0
        while True:
            if cur == tlst[i]:
                cnt += 1
                i += 1
            else:
                break
        if cnt > 1:
            for _ in range(cnt-1):
                tlst.pop(0)
        nlst.append(cnt)
        nlst.append(cur)

    mx_cnt, cnt, flag, cd = 1, 0, 0, 0
    ci,cj = N//2, N//2
    arr = [[0] * N for _ in range(N)]
    if len(nlst) <= N*N-1:
        R = len(nlst)
    else:
        R = N*N-1
    for i in range(R):
        ci, cj = ci + tdi[cd], cj + tdj[cd]
        arr[ci][cj] = nlst[i]
        cnt += 1
        if mx_cnt == cnt:
            cnt = 0
            cd = (cd + 1) % 4
            if flag:
                mx_cnt += 1
                flag = False
            else:
                flag = True

print(ans)