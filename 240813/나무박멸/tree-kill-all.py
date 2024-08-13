N, M, K, C = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]
# 벽을 -1001 처리 (제초제 처리를 위해서)
for i in range(N):
    for j in range(N):
        if arr[i][j] == -1:
            arr[i][j] = -1001
ans = 0
# M년동안 박멸 진행
for turn in range(1,M+1):
    # 0. 제초제 갱신
    for i in range(N):
        for j in range(N):
            if -1001<arr[i][j]<0:
                arr[i][j] += 1

    # 1. 인접한 나무가 있는 수 구하기
    # 1.1 기존 나무 set 구하기
    tree = set()
    for i in range(N):
        for j in range(N):
            if arr[i][j] > 0:
                tree.add((i,j))
                cnt = 0
                for ni, nj in ((i - 1, j), (i, j + 1), (i + 1, j), (i, j - 1)):
                    if 0<=ni<N and 0<=nj<N and arr[ni][nj] > 0:
                        cnt += 1
                arr[i][j] += cnt

    # 2. 기존에 있었던 나무들에서 인접한 4개의 칸 중 벽, 다른 나무, 제초제 모두 없는 칸에 번식을 진행
    for i in range(N):
        for j in range(N):
            if arr[i][j] > 0 and (i,j) in tree:
                # 번식 진행할 나무들
                ntree = set()
                for ni,nj in ((i-1,j),(i,j+1),(i+1,j),(i,j-1)):
                    if 0<=ni<N and 0<=nj<N and (arr[ni][nj] == 0 or ((ni,nj) not in tree and arr[ni][nj] > 0)):
                        ntree.add((ni,nj))
                if not ntree:
                    continue
                cnt = arr[i][j] // len(ntree)
                for ni,nj in ntree: # 번식 진행
                    arr[ni][nj] += cnt
    # 3. 제초제 뿌리기
    # 3.1 k칸 만큼 대각선으로 전파해서 최댓값 구하기
    mx = 0
    si,sj = N,N
    for i in range(N):
        for j in range(N):
            if arr[i][j] > 0:
                tmp = arr[i][j]
                # 4방향 k만큼 전파
                for di,dj in ((-1,-1),(-1,1),(1,-1),(1,1)):
                    for mul in range(1, K + 1):
                        ni, nj = i + di * mul, j + dj * mul
                        # 범위 벗어나거나 벽이거나 나무가 없으면 break
                        if not (0<=ni<N and 0<=nj<N) or -1001 <= arr[ni][nj] < 0:
                        # if not (0 <= ni < N and 0 <= nj < N) or arr[ni][nj] == -1001:
                            break
                        tmp += arr[ni][nj]
                if tmp > mx:
                    mx = max(mx,tmp)
                    si,sj = i,j
    if mx == 0:
        break
    ans += mx
    # 3.2 뿌리기
    if (si,sj) != (N,N):
        arr[si][sj] = -(C+1)
        for di, dj in ((-1, -1), (-1, 1), (1, -1), (1, 1)):
            for mul in range(1, K + 1):
                ni, nj = si + di * mul, sj + dj * mul
                # 범위 벗어나거나 벽이거나 나무가 없으면 break
                if not (0 <= ni < N and 0 <= nj < N):
                    break
                if arr[ni][nj] <= 0:
                    if arr[ni][nj] > -(C+1):
                        arr[ni][nj] = -(C + 1)
                    break
                else:
                    arr[ni][nj] = -(C+1)
print(ans)