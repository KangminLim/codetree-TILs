N, M, K = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]

for _ in range(M):
    si, sj = map(lambda x:int(x)-1,input().split())
    arr[si][sj] -= 1 # 참가자 위치 음수화

ei, ej = map(lambda x: int(x) - 1, input().split())
arr[ei][ej] = -11

ans = 0
cnt = M

def find_square(arr):
    mn = N*N*2
    for i in range(N):
        for j in range(N):
            if -11 < arr[i][j] < 0:
                mn = min(mn,max(abs(ei-i),abs(ej-j)))

    for si in range(N-mn):
        for sj in range(N-mn):
            if si<=ei<=si+mn and sj<=ej<=sj+mn:
                for i in range(mn+1):
                    for j in range(mn+1):
                        if -11 < arr[si+i][sj+j] < 0:
                            return si,sj,mn+1
for turn in range(K):
    narr = [x[:] for x in arr]
    # 1. 모든 참가자 이동
    for i in range(N):
        for j in range(N):
            if -11<arr[i][j]<0: # 사람이면
                dist = abs(ei-i) + abs(ej-j)
                for ni,nj in ((i-1,j),(i+1,j),(i,j-1),(i,j+1)):
                    # 4방향, 범위 내, 벽 x, 거리가 가까워지는
                    if 0<=ni<N and 0<=nj<N and arr[ni][nj] <= 0 and dist > abs(ei-ni) + abs(ej-nj):
                        narr[i][j] -= arr[i][j] # 이동 전 위치 처리
                        ans -= arr[i][j] # 이동 거리 업데이트
                        if arr[ni][nj] == -11: # 출구면
                            cnt += arr[i][j] # 출구에 도착
                        else:
                            narr[ni][nj] += arr[i][j]
                        break
    if cnt == 0: break
    arr = narr

    # 2. 한 명 이상의 참가자와 출구를 포함하는 정사각형 찾기 함수
    si,sj,mn = find_square(arr)

    # 3. 미로 회전, 90도 시계 방향
    narr = [x[:] for x in arr]
    for i in range(mn):
        for j in range(mn):
            narr[si+i][sj+j] = arr[si+mn-1-j][sj+i]
            if narr[si+i][sj+j] >= 1:
                narr[si+i][sj+j] -= 1
    arr = narr

    for i in range(N):
        for j in range(N):
            if arr[i][j] == -11:
                ei,ej = i,j

print(ans)
print(ei+1,ej+1)