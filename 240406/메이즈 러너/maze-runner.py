N, M, K = map(int,input().split())

arr = [list(map(int,input().split())) for _ in range(N)]

for _ in range(M):
    i,j = map(int,input().split())
    arr[i-1][j-1] -= 1

ei,ej = map(lambda x: int(x)-1,input().split())
arr[ei][ej] = -11
cnt = M # 탈출 카운트
ans = 0

def find_square(arr):

    mn = N
    for i in range(N):
        for j in range(N):
            if -11<arr[i][j]<0: # 사람일 경우 출구와 최단거리 찾기 (가로 혹은 세로)
                mn = min(mn, max(abs(ei-i), abs(ej-j)))

    for si in range(N-mn):
        for sj in range(N-mn):
            if si<=ei<=si+mn and sj<=ej<=sj+mn: # 출구가 포함된 사각형의 범위
                for i in range(si,si+mn+1):
                    for j in range(sj,sj+mn+1):
                        if -11 < arr[i][j] < 0:
                            return si,sj, mn+1

for _ in range(K):
    narr = [x[:] for x in arr]
    # [1] 모든 참가자는 한 칸씩 움직임
    for i in range(N):
        for j in range(N):
            if -11<arr[i][j]<0: # 사람일 떄
                 dist = abs(ei-i)+abs(ej-j)
                 for ni,nj in ((i-1,j),(i+1,j),(i,j-1),(i,j+1)):
                    if 0<=ni<N and 0<=nj<N and arr[ni][nj] <= 0 and dist > abs(ei-ni)+abs(ej-nj): # 범위 내, 벽이 아니고, 거리가 짧아지면
                        ans += arr[i][j] # 이동한 거리 더해주기
                        narr[i][j] -= arr[i][j] # 현재 위치 제거
                        if (ni,nj) == (ei,ej): # 출구 위치라면
                            cnt += arr[i][j] # 탈출
                        else:
                            narr[ni][nj] += arr[i][j] # 이동 처리
                        break # 이동하면 끝
    arr = narr

    # 모두 탈출 했으면 종료
    if cnt == 0: break

    # [2] 한 명 이상의 참가자와 출구를 포함한 가장 작은 정사각형 잡기

    narr = [x[:] for x in arr]

    si,sj,L = find_square(arr) # 정사각형 찾기 함수

    # [3] 시계방향 90도 회전 및 회전된벽 내구도 1씩 깎기
    for i in range(L):
        for j in range(L):
            narr[si+i][sj+j] = arr[si+L-j-1][sj+i]
            if narr[si+i][sj+j] > 0:
                narr[si+i][sj+j] -= 1
    arr = narr

    # 회전 후 출구 값 찾기
    for i in range(N):
        for j in range(N):
            if arr[i][j] == -11:
                ei,ej = i, j

print(-ans)
print(ei+1,ej+1)