N, M = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]
di,dj = [0,0,-1,-1,-1,0,1,1,1], [0,1,1,0,-1,-1,-1,0,1]
tlst = [(N-2,0),(N-2,1),(N-1,0),(N-1,1)]
for turn in range(1,M+1):
    cd,mul = map(int,input().split())
    # 1. 특수 영양제 이동
    for i in range(len(tlst)):
        ci,cj = tlst[i]
        ni,nj = (ci+di[cd] * mul)%N, (cj+dj[cd] * mul)%N
        arr[ni][nj] += 1
        tlst[i] = (ni,nj)

    # 2. 특수 영양제 투입
    for i in range(len(tlst)):
        ci,cj = tlst[i]
        for ni,nj in ((ci-1,cj-1),(ci-1,cj+1),(ci+1,cj-1),(ci+1,cj+1)):
            if 0<=ni<N and 0<=nj<N:
                if arr[ni][nj] >= 1:
                    arr[ci][cj] += 1
    nlst = []
    for i in range(N):
        for j in range(N):
            if arr[i][j] >= 2 and (i,j) not in tlst:
                arr[i][j] -= 2
                nlst.append((i,j))

    tlst = nlst

ans = 0
for i in range(N):
    for j in range(N):
        if arr[i][j] > 0:
            ans += arr[i][j]
print(ans)