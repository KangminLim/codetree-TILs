N, K = map(int,input().split())
lst = list(map(int,input().split()))
# lst = [0,1,2,3,4,5]
dlst = [[0] * N for _ in range(2)]

for i in range(2):
    for j in range(N):
        if i==0 and j==N-1:
            dlst[i][j] = 1
        # 좌
        elif i ==1 and 0 < j <= N-1:
            dlst[i][j] = 2
        # 상
        elif i ==1 and j == 0:
            dlst[i][j] = 3
        else:
            dlst[i][j] = 0
k = 0
parr = [[0] * N for _ in range(2)]
arr = [[0] * N for _ in range(2)]
for i in range(2):
    for j in range(N):
        arr[i][j] = lst[k]
        k += 1
plst = []
# 우 하 좌 상
di,dj = [0,1,0,-1],[1,0,-1,0]
M = N//2 # 도착 지점
time = 0
while True:
    cnt = 0
    for a in arr:
        cnt += a.count(0)
    if cnt >= K : break
    time += 1
    # 1. 무빙워크 회전
    narr = [x[:] for x in arr]
    pnarr = [x[:] for x in parr]
    for i in range(2):
        for j in range(N):
            ni,nj = i + di[dlst[i][j]], j + dj[dlst[i][j]]
            narr[ni][nj] = arr[i][j]
            if i == 0: # 무빙워크로 사람도 이동
                if j == N-1:
                    pnarr[i][j] = 0
                else:
                    if parr[i][j] == 1:
                        pnarr[ni][nj] = 1
                        pnarr[i][j] = 0

    parr = pnarr
    arr = narr

    # 2. 첫번쨰 컨테이너에 올림
    for a in arr:
        cnt += a.count(0)
    if cnt >= K : break
    pnarr = [x[:] for x in parr]
    for i in range(1):
        for j in range(N):
            ni, nj = i + di[dlst[i][j]], j + dj[dlst[i][j]]
            if (i,j) == (0,0): # 1번 칸 일 때
                if time == 1:
                    pnarr[i][j] = 1
                    arr[i][j] -= 1

                elif parr[i][j] == 0 and arr[ni][nj] >= 1: # 1번 칸도 비었고,  안정성이 1이상이면 새로 올리기
                    pnarr[i][j] = 1
                    arr[i][j] -=1
            else: # 이동
                if (i,j) == (0,N-1):
                    pnarr[i][j] = 0
                elif parr[i][j] == 1 and parr[ni][nj] == 0 and arr[ni][nj] >= 1:
                    arr[ni][nj] -= 1
                    pnarr[ni][nj] = 1
                    pnarr[i][j] = 0
    parr = pnarr
    for a in arr:
        cnt += a.count(0)
    if cnt >= K : break
print(time)