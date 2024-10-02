N, M, K = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]
for _ in range(M):
    si,sj = map(lambda x:int(x)-1,input().split())
    arr[si][sj] -= 1

ei,ej = map(lambda x:int(x)-1,input().split())
arr[ei][ej] = -11
cnt = M
ans = 0

def find_square(arr):
    mn = N*N*2
    for i in range(N):
        for j in range(N):
            if -11 < arr[i][j] < 0:
                mn = min(mn,max(abs(ei-i),abs(ej-j)))

    for si in range(N-mn):
        for sj in range(N-mn):
            if si<=ei<=si+mn and sj<=ej<=sj+mn:
                for i in range(si,si+mn+1):
                    for j in range(sj,sj+mn+1):
                        if -11 < arr[i][j] < 0:
                            return si,sj,mn+1

def find_exit(arr):
    for i in range(N):
        for j in range(N):
            if arr[i][j] == -11:
                return i,j


for turn in range(1,K+1):

    narr = [x[:] for x in arr]
    # 1. 모든 참가자 이동
    for i in range(N):
        for j in range(N):
            if arr[i][j] < 0:
                dist = abs(ei-i) + abs(ej-j)
                for ni,nj in ((i-1,j),(i+1,j),(i,j-1),(i,j+1)):
                    # 범위 내, 빈칸 혹은 사람 있는 칸, 거리가 가까워지는
                    if 0<=ni<N and 0<=nj<N and arr[ni][nj] <= 0 and dist > abs(ei-ni) + abs(ej-nj):
                        ans -= arr[i][j]
                        narr[i][j] -= arr[i][j]
                        if (ni,nj) == (ei,ej):
                            cnt += arr[i][j]
                        else:
                            narr[ni][nj] += arr[i][j]
                        break
    if cnt == 0:
        break
    arr = narr
    si,sj,mn = find_square(arr)
    narr = [x[:] for x in arr]

    for i in range(mn):
        for j in range(mn):
            narr[si+i][sj+j] = arr[si+mn-j-1][sj+i]
            if narr[si+i][sj+j] > 0:
                narr[si+i][sj+j] -= 1

    arr = narr

    ei,ej = find_exit(arr)

print(ans)
print(ei+1,ej+1)