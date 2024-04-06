N, M, K = map(int,input().split())

arr = [list(map(int,input().split())) for _ in range(N)]


for _ in range(M):
    i,j = map(lambda x: int(x)-1,input().split())
    arr[i][j] -= 1 # 2명 이상 같이 있을 수 있다.

ei,ej = map(lambda x:int(x)-1, input().split())
arr[ei][ej] = -11

def find_square(arr):
    mn = N
    for i in range(N):
        for j in range(N):
            if -11 < arr[i][j] < 0: # 사람일 떄
                mn = min(mn, max(abs(ei-i),abs(ej-j))) # 가장 짧은 가로 혹은 세로 구하기

    for si in range(N-mn):
        for sj in range(N-mn):
            if si <= ei <= si+mn and sj<=ej<=sj+mn: # 출구를 포함한 정사각형
                for i in range(si,si+mn+1):
                    for j in range(sj,sj+mn+1):
                        if -11 < arr[i][j] < 0: # 탈출구 찾으면 탈출
                            return si,sj,mn+1



ans = 0
cnt = M
# K턴 동안 게임 진행
for _ in range(1,K+1):
    # [1] 참가자 이동
    narr = [x[:] for x in arr]
    for i in range(N):
        for j in range(N):
            if -11<arr[i][j]<0: # 사람이면 이동
                dist = abs(ei-i) + abs(ej-j)  # 현재 거리
                for ni, nj in ((i-1,j),(i+1,j),(i,j-1),(i,j+1)): # 상하좌우 이동 (상하 우선)
                    if 0<=ni<N and 0<=nj<N and arr[ni][nj] <= 0 and dist>(abs(ei-ni) + abs(ej-nj)): # 범위 내, 벽이 아니고, 거리가 가까워지면
                        ans += arr[i][j] # 이동거리 더하기
                        narr[i][j] -= arr[i][j] # 이동처리

                        if (ni,nj) == (ei,ej): # 출구인지
                            cnt += arr[i][j] # 도착하면 뺴기

                        else: # 출구가 아닌지
                            narr[ni][nj] += arr[i][j] # 이동
                        break
    arr = narr

    if cnt == 0: break

    # [2] 한 명 이상의 참가자와 출구를 포함한 가장 작은 정사각형 찾기

    narr = [x[:] for x in arr]

    si,sj,L = find_square(arr)


    # [3] 미로 회전

    for i in range(L):
        for j in range(L):
            narr[si+i][sj+j] = arr[si+L-j-1][sj+i]
#            # 벽이면 내구도 1 감소
            if narr[si+i][sj+j] > 0:
                narr[si+i][sj+j] -= 1
    arr = narr

    for i in range(N):
        for j in range(N):
            if arr[i][j] == -11: # 출구 찾기
                ei,ej = i,j

print(-ans)
print(ei+1,ej+1)