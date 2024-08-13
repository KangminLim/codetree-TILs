N, M, K, C = map(int,input().split())
INF = -10000
arr = [[INF] * (N+2)] + [[INF] + list(map(int,input().split())) + [INF] for _ in range(N)] + [[INF] * (N+2)]
for i in range(1,N+1):
    for j in range(1,N+1):
        if arr[i][j] == -1:
            arr[i][j] = INF
ans = 0

for _ in range(1,M+1):

    # 0. 제초제 회복
    for i in range(1,N+1):
        for j in range(1,N+1):
            if -10000 < arr[i][j] < 0:
                arr[i][j] += 1

    # 1. 인접한 네 개의 칸 중 나무가 있는 칸의 수만큼 나무가 성장한다. 성장은 모든 나무에게 동시에 일어난다.
    narr = [x[:] for x in arr]
    for i in range(1,N+1):
        for j in range(1,N+1):
            if arr[i][j] > 0: # 나무일 떄
                for ni,nj in ((i-1,j),(i,j+1),(i+1,j),(i,j-1)):
                    if arr[ni][nj] > 0: # 인접한 네 개의 칸 중 나무가 있는 칸의 수만큼 나무가 성장한다.
                        narr[ni][nj] += 1
    arr = narr
    # 2. 기존에 있었던 나무들은 인접한 4개의 칸 중 벽, 다른 나무, 제초제 모두 없는 칸에 번식을 진행한다.
    narr = [x[:] for x in arr]

    for i in range(1,N+1):
        for j in range(1,N+1):
            if arr[i][j] > 0: # 기존 나무
                tlst = [] # 번식 가능한 나무 리스트
                for ni,nj in ((i-1,j),(i,j+1),(i+1,j),(i,j-1)):
                    if arr[ni][nj] == 0: # 빈 칸만 번식 진행
                        tlst.append((ni,nj))
                # 번식 할 곳 없으면 continue
                if not tlst: continue
                cnt = arr[i][j] // len(tlst)
                for ti,tj in tlst:
                    narr[ti][tj] += cnt
    arr = narr

    # 3. 각 칸 중 제초제를 뿌렸을 때 나무가 가장 많이 박멸되는 칸에 제초제를 뿌리기
    mx,si,sj = 0, N+2, N+2

    # 3.1 가장 많이 박멸되는 칸 찾기
    for i in range(1,N+1):
        for j in range(1,N+1):
            if arr[i][j] > 0:
                tmp = arr[i][j]
                for di, dj in ((-1,-1),(-1,1),(1,-1),(1,1)):
                    for mul in range(1,K+1):
                        ni,nj = i + di * mul, j + dj * mul
                        if arr[ni][nj] <= 0: # 나무가 아니면 뿌리기 취소
                            break
                        else:
                            tmp += arr[ni][nj]
                if tmp > mx:
                    mx = max(mx, tmp)
                    si,sj = i,j
    # 3.2 제초제 뿌리기
    if mx == 0: break # 종료조건
    else : ans += mx
    narr = [x[:] for x in arr]

    narr[si][sj] = -(C+1)
    for di, dj in ((-1, -1), (-1, 1), (1, -1), (1, 1)):
        for mul in range(1, K + 1):
            ni, nj = si + di * mul, sj + dj * mul
            if arr[ni][nj] <= 0:  # 나무가 아니면 뿌리기 취소
                if arr[ni][nj] >= -(C+1): # 제초제보다 크면 뿌리기
                    narr[ni][nj] = -(C+1)
                break
            else:
                narr[ni][nj] = -(C+1)

    arr = narr

print(ans)