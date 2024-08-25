N, M = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]
di, dj = [0,0,-1,-1,-1,0,1,1,1], [0,1,1,0,-1,-1,-1,0,1]
tree = [(N-2,0),(N-2,1),(N-1,0),(N-1,1)]
for turn in range(1,M+1):
    dr, mul = map(int,input().split())
    # 리브로수 체크를 위한 tset
    tlst = []
    for i in range(len(tree)):
        ci, cj = tree[i]
        ni, nj = (ci+di[dr]*mul)%N, (cj+dj[dr]*mul)%N
        arr[ni][nj] += 1 # 이동 후 +1
        tlst.append((ni,nj))

    # 4방향 대각선 1이상 나온 개수 만큼 증가
    for i in range(len(tlst)):
        ni, nj = tlst[i]
        for tni,tnj in ((ni-1,nj-1),(ni-1,nj+1),(ni+1,nj-1),(ni+1,nj+1)):
            if 0<=tni<N and 0<=tnj<N and arr[tni][tnj] >= 1:
                arr[ni][nj] += 1

    ntree = []
    for i in range(N):
        for j in range(N):
            if (i,j) not in tlst and arr[i][j] >= 2:
                arr[i][j] -= 2
                ntree.append((i,j))
    tree = ntree

ans = 0
for i in range(N):
    for j in range(N):
        if arr[i][j] > 0:
            ans += arr[i][j]

print(ans)