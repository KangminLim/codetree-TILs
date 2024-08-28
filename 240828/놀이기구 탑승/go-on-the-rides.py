n = int(input())
arr = [[0] * n for _ in range(n)]
fdict = {}
tdict = {}
for idx in range(n*n):
    n0,n1,n2,n3,n4 = map(int,input().split())
    # 순서, 학생 번호, 좋아하는 학생 번호
    fdict[idx] = [n0,n1,n2,n3,n4]
    tdict[n0] = [n1,n2,n3,n4]
adict = {0:0, 1:1, 2:10,3:100,4:1000}
for idx in range(n*n):

    # 1. 격자를 벗어나지 않은 4방향으로 인접한 칸 중 앉아있는 좋아하는 친구의 수가 가장 많은 위치로 간다.
    # 1.1 배치할 자리 찾기
    fcnt, zcnt, tcnt = 0,0,0
    tfi,tfj = n,n
    tzi,tzj = n,n
    tlst = []
    for ci in range(n):
        for cj in range(n):
            tfcnt, tzcnt = 0, 0
            # 빈 칸 이동
            if arr[ci][cj] == 0:
                for ni, nj in ((ci-1,cj),(ci,cj+1),(ci+1,cj),(ci,cj-1)):
                    # 범위 내
                    if 0<=ni<n and 0<=nj<n:
                        if arr[ni][nj] in fdict[idx]: # 좋아하는 친구가 있다면
                            tfcnt += 1
                        elif arr[ni][nj] == 0:
                            tzcnt += 1
                tlst.append((tfcnt,tzcnt,ci,cj))

    tlst.sort(key = lambda x:(-x[0],-x[1],x[2],x[3]))
    if tlst:
        ti, tj = tlst[0][2], tlst[0][3]
        arr[ti][tj] = fdict[idx][0]
    else:
        for i in range(n):
            for j in range(n):
                if arr[i][j] == 0:
                    arr[i][j] = fdict[idx][0]


ans = 0
for ci in range(n):
    for cj in range(n):
        cur = arr[ci][cj]
        tfcnt = 0
        # 빈 칸 이동
        for ni, nj in ((ci - 1, cj), (ci, cj + 1), (ci + 1, cj), (ci, cj - 1)):
            # 범위 내
            if 0 <= ni < n and 0 <= nj < n:
                if arr[ni][nj] in tdict[cur]:  # 좋아하는 친구가 있다면
                    tfcnt += 1
        ans += adict[tfcnt]

print(ans)