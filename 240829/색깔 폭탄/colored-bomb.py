N, M = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]

ans = 0
from collections import deque
def bfs(si,sj):
    q = deque()
    q.append((si,sj))
    v = [[False] * N for _ in range(N)]
    v[si][sj] = True
    tmp, tmp_red, tmp_lst = 1, 0, [(si,sj)]
    while q:
        ci,cj = q.popleft()
        for ni,nj in ((ci-1,cj),(ci+1,cj),(ci,cj-1),(ci,cj+1)):
            if 0<=ni<N and 0<=nj<N and not v[ni][nj] and (arr[si][sj] == arr[ni][nj] or arr[ni][nj] == 0):
                q.append((ni,nj))
                v[ni][nj] = True
                tmp += 1
                tmp_lst.append((ni,nj))
                if arr[ni][nj] == 0:
                    tmp_red += 1

    return tmp, tmp_red, tmp_lst


# 폭탄 묶음 없을 때까지
while True:
    # 1. 크기가 큰 폭탄 묶음 찾기
    mx, mn_red, mx_lst = 0, N**2, []
    # 행이 큰, 열이 작은
    for i in range(N-1,-1,-1):
        for j in range(N):
            if arr[i][j] > 0: # 색깔 폭탄
                tmp, tmp_red, tmp_lst = bfs(i,j)
                # 1.1 크기가 가장 큰 폭탄 묶음
                if tmp > mx:
                    mx = tmp
                    mn_red = tmp_red
                    mx_lst = tmp_lst
                # 1.2 빨간색 폭탄이 가장 적게 포함된 것
                elif tmp == mx:
                    if tmp_red < mn_red:
                        mn_red = tmp_red
                        mx_lst = tmp_lst
    if 2 > mx:
        break
    ans += mx ** 2

    # tlst = [x[:] for x in arr]
    # 3.1 폭탄 제거
    for ti,tj in mx_lst:
        arr[ti][tj] = -10

    # t1lst = [x[:] for x in arr]
    # print('')
    # 3.2 중력 작용
    narr = [x[:] for x in arr]

    for j in range(N): # 열
        for i in range(N-1,-1,-1): # 행
            if arr[i][j] >= 0:
                while True:
                    ni = i + 1
                    if not (0 <= ni < N) or narr[ni][j] >= -1:
                        break
                    else:
                        narr[ni][j] = narr[i][j]
                        narr[i][j] = -10
                        i = ni
    arr = narr
    # t2lst = [x[:] for x in arr]
    # print('')
    # 4.1 반시계 90도 회전
    narr = [x[:] for x in arr]
    for i in range(N):
        for j in range(N):
            narr[i][j] = arr[j][N-1-i]
    arr = narr
    # t3lst = [x[:] for x in arr]
    # print('')
    # 4.2 중력
    narr = [x[:] for x in arr]
    for j in range(N): # 열
        for i in range(N-1,-1,-1): # 행
            if arr[i][j] >= 0:
                while True:
                    ni = i + 1
                    if not (0 <= ni < N) or narr[ni][j] >= -1:
                        break
                    else:
                        narr[ni][j] = narr[i][j]
                        narr[i][j] = -10
                        i = ni
    arr = narr
    # t4lst = [x[:] for x in arr]
    # print('')
print(ans)