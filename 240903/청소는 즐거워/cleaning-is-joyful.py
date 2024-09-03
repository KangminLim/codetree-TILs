N = int(input())
arr = [list(map(int,input().split())) for _ in range(N)]
mn_cnt, cnt, flag, dr = 1, 0, 0, 0
di, dj = [0,1,0,-1], [-1,0,1,0] # 좌, 하, 우, 상
ci, cj = N//2, N//2
ans = 0
# 2%, 10%, 7%, 1%, 5%, 10%, 7%, 1%, 2%
mlst = [0.02,0.1,0.07,0.01,0.05,0.1,0.07,0.01,0.02]
tdict = { 0 : [(-2, 0), (-1, -1), (-1, 0), (-1, 1), (0, -2), (1, -1), (1, 0), (1, 1), (2, 0)],
          1 : [(0,-2),(1,-1),(0,-1),(-1,-1),(2,0),(1,1),(0,1),(-1,1),(0,2)],
          2 : [(-2, 0), (-1, 1), (-1, 0), (-1, -1), (0, 2), (1, 1), (1, 0), (1, -1), (2, 0)],
          3 : [(0,-2),(-1,-1),(0,-1),(1,-1),(-2,0),(-1,1),(0,1),(1,1),(0,2)]
         }
ttdict = { 0: (0,-1),
           1: (1,0),
           2: (0,1),
           3: (-1,0)}

# dlst = [(-2,0),(-1,-1),(-1,0),(-1,1),(0,-2),(1,-1),(1,0),(1,1),(2,0)]


# while True:
for k in range(1,N**2+1):
    if (ci,cj) == (0,0):
        break
    narr = [x[:] for x in arr]

    ni,nj = ci+di[dr], cj+dj[dr]
    a = 0 # a값
    # 2%, 10%, 7%, 1%, 5%, 10%, 7%, 1%, 2%
    for i in range(9):
        tdi, tdj = tdict[dr][i]
        tni, tnj = ni + tdi, nj + tdj
        mul = mlst[i]
        tmp = int(arr[ni][nj] * mul)
        a += tmp
        if 0<=tni<N and 0<=tnj<N:
            narr[tni][tnj] = arr[tni][tnj] + tmp
        else:
            ans += tmp
    # a값 처리
    tdi,tdj = ttdict[dr]
    tni,tnj = ni + tdi, nj + tdj
    if 0 <= tni < N and 0 <= tnj < N:
        narr[tni][tnj] = arr[tni][tnj] + (arr[ni][nj]-a)
    else:
        ans += (arr[ni][nj]-a)
    narr[ni][nj] = 0
    arr = narr
    ci,cj = ni,nj
    cnt += 1
    if mn_cnt == cnt:
        cnt = 0
        dr = (dr + 1) % 4

        if flag:
            flag = 0
            mn_cnt += 1
        else:
            flag = 1

print(ans)