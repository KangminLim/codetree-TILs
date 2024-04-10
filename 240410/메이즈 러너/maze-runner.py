N, M, K = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]

for _ in range(M):
    i, j = map(lambda x: int(x)-1,input().split())
    arr[i][j] -= 1

ei,ej = map(lambda x:int(x)-1, input().split())
arr[ei][ej] = -11
ans = 0
cnt = M

def find_square(arr):
    mn = N
    for i in range(N):
        for j in range(N):
            if -11 < arr[i][j] < 0 : # 사람이면
                mn = min(mn, max(abs(ei-i),abs(ej-j))) # 정사각형 최소 길이 찾기 사람을 포함한

    for si in range(N-mn):
        for sj in range(N-mn):
            if si<=ei<=si+mn and sj<=ej<=sj+mn:
                for i in range(si,si+mn+1):
                    for j in range(sj,sj+mn+1):
                        if -11 < arr[i][j] < 0:
                            return si,sj,mn+1



for k in range(1,K+1):
    # 움직이는 조건
    narr = [x[:] for x in arr]
    for i in range(N):
        for j in range(N):
            if -11<arr[i][j]<0: # 사람이면
                dist = abs(ei-i) + abs(ej-j)
                for ni,nj in ((i-1,j),(i+1,j),(i,j-1),(i,j+1)):
                    if 0<=ni<N and 0<=nj<N and arr[ni][nj] <= 0 and dist > abs(ei-ni)+abs(ej-nj):
                        narr[i][j] -= arr[i][j] # 이동처리
                        ans += arr[i][j] # 거리 추가
                        if (ni,nj) == (ei,ej): # 도착
                            cnt += arr[i][j]
                        else:
                            narr[ni][nj] += arr[i][j] # 이동
                        break
    # 미로 회전
    arr = narr

    if cnt == 0 : break

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
                ei,ej = i,j


print(-ans)
print(ei+1,ej+1)