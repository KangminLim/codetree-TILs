N, M, K, C = map(int,input().split())
arr = [[-1001] * (N+2)] + [[-1001] + list(map(int,input().split())) + [-1001] for _ in range(N)] + [[-1001] * (N+2)]
for i in range(1,N+1):
    for j in range(1,N+1):
        if arr[i][j] == -1:
            arr[i][j] = -1001
ans = 0

for t in range(1,M+1):

    # 0. 제초제 업데이트
    for i in range(1,N+1):
        for j in range(1,N+1):
            if -1001< arr[i][j] < 0:
                arr[i][j] += 1
    narr = [x[:] for x in arr]
    # 1. 나무의 성장
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            if arr[i][j]>0:
                cnt = 0
                for ni,nj in ((i-1,j),(i,j+1),(i+1,j),(i,j-1)):
                    if arr[ni][nj] > 0: # 나무가 있으면
                        cnt +=1
                narr[i][j] += cnt
    arr = narr
    narr = [x[:] for x in arr]
    # 2. 나무의 번식
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            if arr[i][j]>0:
                tlst = []
                for ni,nj in ((i-1,j),(i,j+1),(i+1,j),(i,j-1)):
                    if arr[ni][nj] == 0: # 나무가 없으면
                        tlst.append((ni,nj))
                if tlst:
                    for ti, tj in tlst:
                        narr[ti][tj] += arr[i][j] // len(tlst)
    arr = narr
    print('')
    # 3.1 제초제 뿌릴 위치 찾기
    mx,mi,mj = 0,2*N,2*N
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            if arr[i][j] > 0:
                tmp = arr[i][j]
                for di,dj in ((-1,-1),(-1,1),(1,1),(1,-1)):
                    for mul in range(1,K+1):
                        ci,cj = i + di*mul, j + dj*mul
                        if arr[ci][cj] > 0:
                            tmp += arr[ci][cj]
                        else:
                            break
                if tmp > mx:
                    mx = tmp
                    mi,mj = i, j

    if mx == 0:
        break
    ans += mx
    # 3.2 제초제 뿌리기
    arr[mi][mj] = -(C+1)
    narr = [x[:] for x in arr]
    for di, dj in ((-1, -1), (-1, 1), (1, 1), (1, -1)):
        for mul in range(1, K + 1):
            ci, cj = mi + di * mul, mj + dj * mul
            if arr[ci][cj] > 0:
                narr[ci][cj] = -(C+1)
            else:
                if arr[ci][cj] > -(C+1):
                    narr[ci][cj] = -(C+1)
                break
    arr = narr
print(ans)