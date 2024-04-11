N, M, K = map(int,input().split())

arr = [list(map(int,input().split())) for _ in range(N)]

for _ in range(M):
    i,j = map(lambda x: int(x)-1,input().split())
    arr[i][j] -= 1 # 사람을 음수 처리(한 칸에 2명 이상 있을 수 있다)

ei, ej = map(lambda x:int(x)-1, input().split())
arr[ei][ej] = -11

ans = 0 # 총 이동거리
cnt = M # 탈출 했는지 확인

def find_square(arr):
    mn = N
    for i in range(N):
        for j in range(N):
            if -11<arr[i][j]<0:
                mn = min(mn,max(abs(ei-i),abs(ej-j)))

    for ni in range(N-mn):
        for nj in range(N-mn):
            if ni<=ei<=ni+mn and nj<=ej<=nj+mn:
                for i in range(ni,ni+mn+1):
                    for j in range(nj,nj+mn+1):
                        if -11 < arr[i][j] < 0:
                            return ni,nj,mn+1

for k in range(1,K+1):
    narr = [x[:] for x in arr]
    for i in range(N):
        for j in range(N):
            if -11 < arr[i][j] < 0: # 사람이면
                dist = abs(ei-i) + abs(ej-j)
                for ni, nj in ((i-1,j),(i+1,j),(i,j-1),(i,j+1)):
                    # 범위 내, 빈 칸 or 사람 있는 곳 or 출구, 최단거리가 가까워야 한다
                    if 0<=ni<N and 0<=nj<N and arr[ni][nj] <= 0 and dist > abs(ei-ni)+abs(ej-nj):
                        ans += arr[i][j] # 이동거리 누적
                        narr[i][j] -= arr[i][j] # 이동처리
                        if (ni,nj) == (ei,ej): # 도착했다면
                            cnt += arr[i][j]
                        else:
                            narr[ni][nj] += arr[i][j]  # 이동처리
                        break # 한번 이동하면 끝
    arr = narr

    if cnt == 0 : break # 모두 탈출하면 끝

    # 한 명 이상의 참가자와 출구를 포함한 가장 작은 정사각형 잡기
    si,sj,L = find_square(arr)

    narr = [x[:] for x in arr]

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