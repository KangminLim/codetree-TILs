N,M,K = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]
for _ in range(M):
    si,sj = map(lambda x:int(x)-1, input().split())
    arr[si][sj] = -1 # 초기 좌표
ei,ej = map(lambda x:int(x)-1, input().split())
arr[ei][ej] = -11
ans = 0
cnt = N

def find_square(arr):
    mn = N
    for i in range(N):
        for j in range(N):
            if -11<arr[i][j]<0: # 참가자일 때
                dist = max(abs(ei-i),abs(ej-j))
                mn = min(mn,dist)
    for si in range(N-mn):
        for sj in range(N-mn):
            if si<=ei<=si+mn and sj<=ej<=sj+mn:
                for i in range(si,si+mn+1):
                    for j in range(sj,sj+mn+1):
                        if -11<arr[i][j]<0:
                            return si,sj,mn+1

for turn in range(1,K+1):
    narr = [x[:] for x in arr]
    # 1. 모든 참가자가 동시에 이동
    for i in range(N):
        for j in range(N):
            if -11<arr[i][j]<=-1: # 참가자일 때
                dist = abs(ei-i)+abs(ej-j)
                for di,dj in ((-1,0),(1,0),(0,-1),(0,1)):
                    ni,nj = i+di,j+dj
                    new_dist = abs(ei - ni) + abs(ej - nj)
                    if 0<=ni<N and 0<=nj<N and arr[ni][nj] <= 0 and dist>new_dist: # 범위 내, 벽 x, 거리 가까워져야함
                        if (ni,nj) == (ei,ej): # 탈출
                            ans += arr[i][j]
                            cnt += arr[i][j]
                            narr[i][j] = 0 # 이동처리
                        else: # 이동
                            ans += arr[i][j]
                            narr[i][j] -= arr[i][j]
                            narr[ni][nj] += arr[i][j]
                        break
    arr = narr
    if cnt == 0: break
    # 2. 미로 회전
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