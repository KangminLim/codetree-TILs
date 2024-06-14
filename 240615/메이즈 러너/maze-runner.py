N, M, K = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]

for _ in range(M):
    i,j = map(lambda x:int(x)-1, input().split())
    arr[i][j] -= 1

ei,ej = map(lambda x:int(x)-1,input().split())
arr[ei][ej] = -11

ans = 0
cnt = M
# cnt가 0이 되면 모두 탈출

def find_square(arr):
    narr = [x[:] for x in arr]
    mn = N
    for i in range(N):
        for j in range(N):
            if -11 < arr[i][j] < 0: # 사람이면
                mn = min(mn,max(abs(ei-i),abs(ej-j)))

    for si in range(N):
        for sj in range(N):
            if si<=ei<=si+mn and sj<=ej<=sj+mn:
                for i in range(si,si+mn+1):
                    for j in range(sj,sj+mn+1):
                        if -11<arr[i][j]<0:
                            return si,sj,mn+1

for turn in range(1,K+1):
    # 모든 참가자 동시에 움직이기
    narr = [x[:] for x in arr]
    for i in range(N):
        for j in range(N):
            if arr[i][j] < 0:
                dist = abs(ei-i) + abs(ej-j)
                for ni,nj in ((i-1,j),(i+1,j),(i,j-1),(i,j+1)): #상하좌우 우선순위
                    ndist = abs(ei-ni) + abs(ej-nj)
                    if 0<=ni<N and 0<=nj<N and arr[ni][nj] <= 0 and dist > ndist: # 범위내, 벽이 없는 곳, 거리 가까워지는 곳
                        ans += arr[i][j] # 이동거리 누적
                        narr[i][j] -= arr[i][j] # 이동 처리
                        if (ni,nj) != (ei,ej): # 출구가 아니면
                            narr[ni][nj] += arr[i][j] # 이동 처리
                        else: # 출구면
                            cnt += arr[i][j]
                        break

    if cnt == 0: break

    arr = narr

    # 한명 이상의 참가자와 출구를 포함한 가장 작은 정사각형 찾기
    si,sj,L = find_square(arr)

    narr = [x[:] for x in arr]
    for i in range(L):
        for j in range(L):
            narr[si+i][sj+j] = arr[si+L-j-1][sj+i]
            if narr[si+i][sj+j] > 0: # 회전할 때 내구도 감소
                narr[si+i][sj+j] -= 1

    arr = narr

    for i in range(N):
        for j in range(N):
            if arr[i][j] == -11:
                ei,ej = i,j

print(-ans)
print(ei+1,ej+1)