N = int(input())
arr = [[0] * N for _ in range(N)]
lst = [list(map(int,input().split())) for _ in range(N*N)]
fdict = {}
for i in range(N*N):
    n0,n1,n2,n3,n4 = lst[i]
    fdict[n0] = (n1,n2,n3,n4)
adict = {0:0,1:1,2:10,3:100,4:1000}

for i in range(len(lst)):
    fcnt = zcnt = 0
    n0,n1,n2,n3,n4 = lst[i]
    flag = True
    if i == len(lst)-1:
        for si in range(N):
            for sj in range(N):
                if arr[si][sj] == 0:
                    arr[si][sj] = n0
                    flag = False
                    break
            if not flag:
                break
        if not flag:
            break
    tlst = []
    for si in range(N):
        for sj in range(N):
            if arr[si][sj] > 0: continue
            tfcnt = tzcnt = 0
            for ni, nj in ((si-1,sj),(si,sj+1),(si+1,sj),(si,sj-1)):
                if 0<=ni<N and 0<=nj<N:
                    if arr[ni][nj] in (n1,n2,n3,n4):
                        tfcnt += 1
                    elif arr[ni][nj] == 0:
                        tzcnt += 1
            tlst.append((tfcnt,tzcnt,si,sj))
    tlst.sort(key=lambda x:(-x[0],-x[1]))
    ci,cj = tlst[0][2],tlst[0][3]
    arr[ci][cj] = n0

ans = 0
for i in range(N):
    for j in range(N):
        cnt = 0
        for ni,nj in ((i-1,j),(i,j+1),(i+1,j),(i,j-1)):
            if 0<=ni<N and 0<=nj<N and arr[ni][nj] in fdict[arr[i][j]]:
                cnt += 1
        ans += adict[cnt]
print(ans)
