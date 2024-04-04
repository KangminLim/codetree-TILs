# 제초제 음수화가 중요
INF = -10000 # 벽
N, M, K, C = map(int,input().split())
C = -(C+1) # 제초제는 음수처리(C+1년 후에 사라짐)
arr = [[INF] * (N+2)] + [[INF] + list(map(int,input().split())) + [INF] for _ in range(N)] + [[INF] * (N+2)]

for i in range(1,N+1):
    for j in range(1,N+1):
        if arr[i][j] == -1:
            arr[i][j] = INF

ans = 0
for _ in range(M): # M년동안 진행
    # [0] 1년의 시작 (제초제 감소)
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            if arr[i][j] < 0: # 제초제가 뿌려져 있다면 감소 (건물은 -10000 이므로 절대 0 되지 않음)
                arr[i][j] += 1

    # [1] 인접한 네칸 중 나무 있는 칸 수만큼 동시에 성장
    narr = [x[:] for x in arr]

    for i in range(1,N+1):
        for j in range(1,N+1):
            if arr[i][j] > 0: # 나무가 있다면, 인접 나무 수만큼 성장
                for ni,nj in ((i-1,j),(i+1,j),(i,j-1),(i,j+1)): # 둘러 쌓아서 범위 체크 X
                    if arr[ni][nj] > 0:
                        narr[i][j] += 1
    arr = narr

    # [2] 인접한 빈칸에 번식(나무 수 // 빈칸 수 => 동시)

    narr = [x[:] for x in arr]

    for i in range(1,N+1):
        for j in range(1,N+1):
            if arr[i][j] > 0: # 내가 나무면 번식
                tlst = [] # 빈칸 좌표 저장
                for ni, nj in ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)):  # 둘러 쌓아서 범위 체크 X
                    if arr[ni][nj] == 0:
                        tlst.append((ni,nj))
                if tlst: # 빈칸이 있는 경우 => 번식
                    d = arr[i][j] // len(tlst)
                    for ti,tj in tlst:
                        narr[ti][tj] += d

    arr = narr

    # [3-1] 가장 많이 박멸되는 칸을 찾기
    mx, mx_i, mx_j = 0,0,0
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            if arr[i][j] > 0: # 나무 있는 칸에 뿌려야 제초됨
                cnt = arr[i][j] # 내 자리(중심) 포함
                for di, dj in ((-1,-1),(-1,1),(1,-1),(1,1)):
                    for mul in range(1,K+1): #  뻗어가면서 처리
                        ni, nj = i + di*mul, j + dj*mul
                        if arr[ni][nj] <= 0: # 빈 땅, 제초제, 건물
                            break # 그 방향은 그만
                        else:  # 나무 있는 경우
                            cnt += arr[ni][nj]
                # 최댓값이면 갱신
                if mx < cnt:
                    mx, mx_i, mx_j = cnt, i, j

    if mx == 0: # 0이라면 나무가 한 그루도 없는 것 => break
        break
    ans += mx

    # [3-2] 제초제 살포
    # 전파되는 도중 벽이 있거나 나무가 아얘 없는 칸이 있는 경우, 그 칸 까지는 제초제가 뿌려지며 그 이후의 칸으로는 제초제가 전파되지 않습니다.
    arr[mx_i][mx_j] = C # 중앙 자리에 제초제 뿌림
    for di, dj in ((-1, -1), (-1, 1), (1, -1), (1, 1)):
        for mul in range(1, K + 1):  # 뻗어가면서 처리
            ni, nj = mx_i + di * mul, mx_j + dj * mul
            # 벽(건물)에 제촙제 뿌리면 시간이 지나면 빈땅이 됨
            if arr[ni][nj] <= 0: # 뻗어가는 것이 종료되는 조건: 빈땅, 제초제 뿌려진 빈 땅 / 벽(건물)을 제외
                if C<=arr[ni][nj]: # 제초제 뿌리는 조건
                    arr[ni][nj] = C # 뿌리고, break
                break
            else: # 나무면
                arr[ni][nj] = C

print(ans)