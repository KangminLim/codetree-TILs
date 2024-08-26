N, M = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]
# 타워 방향 : 우, 하, 좌, 상
tdi,tdj = [0,1,0,-1], [1,0,-1,0]
# 달팽이 이동 : 좌, 하, 우, 상
di, dj = [0,1,0,-1], [-1,0,1,0]

HN = N//2
arr[HN][HN] = -1
ans = 0
from collections import deque

for turn in range(1,M+1):
    dr, P = map(int,input().split())
    tmp_N = N * N
    for l in arr:
        tmp_N -= l.count(0)

    # 1. 중앙 탑에서 공격
    for mul in range(1,P+1):
        ti,tj = HN + tdi[dr] * mul, HN + tdj[dr] * mul
        ans += arr[ti][tj]
        arr[ti][tj] = 0

    # 2. 비어있는 공간 채우기
    # 2.1 달팽이 이동 : 달팽이 이동하면서 arr[i][j] > 0 queue에 추가
    while True:
        mn_cnt, cnt, flag, cd = 1, 0, 0, 0
        ci, cj = HN,HN
        tlst = deque()
        for k in range(1,tmp_N+1):
            ci, cj = ci + di[cd], cj + dj[cd]
            cnt += 1
            if arr[ci][cj] > 0:
                tlst.append(arr[ci][cj])

            if mn_cnt == cnt:
                cnt = 0
                cd = (cd+1) % 4
                if flag:
                    mn_cnt += 1
                    flag = 0
                else:
                    flag = 1
        # 2.1 빈 칸 달팽이 채우기
        # 2.2 tlst 채우기부터 해야함
        ttlst = tlst.copy()
        cnt = 0
        nlst = []
        tmp = 0
        while len(tlst)>1:
            cur = tlst.popleft()
            if cur == tlst[0]:
                cnt += 1
            else:
                if cnt >= 3:
                    tmp = cur * (cnt+1)
                    ans += tmp
                    cnt = 0
                else:
                    if cnt >=1:
                        for _ in range(cnt+1):
                            nlst.append(cur)
                    else:
                        nlst.append(cur)
                    cnt = 0
        if 2 >= cnt >0:
            for _ in range(cnt+1):
                nlst.append(cur)
        elif cur == tlst[0] and cnt > 2:
            ans += cur * (cnt+1)
            break
        else:
            nlst.append(tlst.pop())
        if tmp == 0:
            cnt = 0
            nlst = []
            tmp = 0
            while len(ttlst) > 1:
                cur = ttlst.popleft()
                if cur == ttlst[0]:
                    cnt += 1
                else:
                    nlst.append(cnt + 1)
                    nlst.append(cur)
                    cnt = 0
            nlst.append(cnt+1)
            nlst.append((ttlst.pop()))

            narr = [[0] * N for _ in range(N)]
            mn_cnt, cnt, flag, cd = 1, 0, 0, 0
            ci, cj = HN, HN

            tmp_N = len(nlst)
            if tmp_N > N*N:
                tmp_N = N*N
            for k in range(tmp_N):
                ci, cj = ci + di[cd], cj + dj[cd]
                cnt += 1
                narr[ci][cj] = nlst[k]

                if mn_cnt == cnt:
                    cnt = 0
                    cd = (cd + 1) % 4
                    if flag:
                        mn_cnt += 1
                        flag = 0
                    else:
                        flag = 1
            arr = narr
            break
        narr = [[0] * N for _ in range(N)]
        mn_cnt, cnt, flag, cd = 1, 0, 0, 0
        ci, cj = HN, HN

        tmp_N = len(nlst)
        for k in range(tmp_N):
            ci, cj = ci + di[cd], cj + dj[cd]
            cnt += 1
            narr[ci][cj] = nlst[k]

            if mn_cnt == cnt:
                cnt = 0
                cd = (cd + 1) % 4
                if flag:
                    mn_cnt += 1
                    flag = 0
                else:
                    flag = 1

        arr = narr
print(ans)