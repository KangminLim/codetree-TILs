N, M, K = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]

for _ in range(M):
    i,j = map(lambda x : int(x)-1, input().split())
    arr[i][j] -= 1

ei, ej = map(lambda x : int(x)-1, input().split())
arr[ei][ej] = -11

ans = 0
cnt = M

def find_square(arr):

    mn = N
    for i in range(N):
        for j in range(N):
            if -11 < arr[i][j] < 0: # 사람일 때
                mn = min(mn,max(abs(ei-i),abs(ej-j))) # 최소 사각형 길이

    for si in range(N-mn):
        for sj in range(N-mn):
            if si<=ei<=si+mn and sj<=ej<=sj+mn:
                for i in range(si,si+mn+1):
                    for j in range(sj,sj+mn+1):
                        if -11 < arr[i][j] < 0:
                            return si,sj,mn+1

# K턴 동안 진행
for turn in range(1,K+1):
    narr = [x[:] for x in arr]

    # [1] 모든 참가자가 한 칸 씩 이동
    for i in range(N):
        for j in range(N):
            if arr[i][j] <= 0: # 벽이 아닌 곳
                dist = abs(ei-i) + abs(ej-j)
                for ni,nj in ((i-1,j),(i+1,j),(i,j-1),(i,j+1)):
                    if 0<=ni<N and 0<=nj<N and arr[ni][nj] <=0 and dist > abs(ei-ni) + abs(ej-nj): # 범위내, 거리가 가까워지는 곳으로 이동
                        narr[i][j] -= arr[i][j] # 이동 처리
                        ans += arr[i][j] # 이동거리 누적
                        if arr[ni][nj] == -11: # 출구라면
                            cnt += arr[i][j]
                        else: # 빈칸이면
                            narr[ni][nj] += arr[i][j] # 이동처리
                        break

    arr = narr

    if cnt ==0:
        break
    # [2] 미로 회전
    si,sj,L = find_square(arr)

    narr = [x[:] for x in arr]

    # 90도 회전
    for i in range(L):
        for j in range(L):
            narr[si+i][sj+j] = arr[si+L-j-1][sj+i]
            if narr[si+i][sj+j] > 0:
                narr[si+i][sj+j] -= 1

    arr = narr

    for i in range(N):
        for j in range(N):
            if arr[i][j] == -11:
                ei,ej = i, j

print(-ans)
print(ei+1,ej+1)