N = int(input())
flst = []
fdict = {}
for i in range(N*N):
    n0,n1,n2,n3,n4 = map(int,input().split())
    flst.append((n0,n1,n2,n3,n4))
    fdict[n0] = (n1,n2,n3,n4)
arr = [[0] * N for _ in range(N)]

for i in range(N*N):
    n0, n1, n2, n3, n4 = flst[i]
    tlst = []
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 0:
                cnt1, cnt2 = 0, 0

                for ni, nj in ((i-1,j),(i,j+1),(i+1,j),(i,j-1)):
                    if 0<=ni<N and 0<=nj<N:
                        if arr[ni][nj] > 0 and arr[ni][nj] in (n1,n2,n3,n4):
                            cnt1 += 1
                        elif arr[ni][nj] == 0:
                            cnt2 += 1
                tlst.append((cnt1,cnt2,i,j))
    tlst.sort(key=lambda x:(-x[0],-x[1],x[2],x[3]))
    ci,cj = tlst[0][2],tlst[0][3]
    arr[ci][cj] = n0

ans = 0
adict = {0:0,1:1,2:10,3:100,4:1000}


for i in range(N):
    for j in range(N):
        cur = arr[i][j]
        cnt = 0
        for ni, nj in ((i - 1, j), (i, j + 1), (i + 1, j), (i, j - 1)):
            if 0 <= ni < N and 0 <= nj < N:
                if arr[ni][nj] in fdict[cur]:
                    cnt += 1
        ans += adict[cnt]
print(ans)