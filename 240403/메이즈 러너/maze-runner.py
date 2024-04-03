N, M, K = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]

for _ in range(M):
    i,j = map(lambda x: int(x)-1,input().split())
    arr[i][j] -= 1 # 동일한 좌표에서 시작할 수도 있음

ei,ej = map(lambda x: int(x)-1, input().split())
arr[ei][ej] = -11 # 출구 좌표

# 한 명 이상의 참가자와 출구를 포함한 가장 작은 정사각형 찾기 / r 좌표 작은 것 우선 / c 좌표 작은 것 우선
def find_square(arr):
    mn = N # 정사각형 길이 / 출구와 참가자의 최소 거리 찾기
    for i in range(N):
        for j in range(N):
            if -11< arr[i][j] < 0: # 사람일 경우
                mn = min(mn, max(abs(ei-i),(abs(ej-j)))) # 가장 짧은 정사각형 가로 or 세로 찾기

    for si in range(N-mn):
        for sj in range(N-mn):
            if si <= ei <= si+mn and sj <= ej <= sj+mn: # 출구를 포함한 정사각형이라면
                for i in range(si+mn+1):
                    for j in range(sj+mn+1):
                        if -11< arr[i][j] <0:
                            return si,sj,mn+1
def find_exit(arr):
    for i in range(N):
        for j in range(N):
            if arr[i][j] == -11:
                return i, j

# K턴 동안 반복
ans = 0
cnt = M

for turn in range(1,K+1):
    # [1] 모든 참가자 한 칸씩 이동
    narr = [x[:] for x in arr]
    for i in range(N):
        for j in range(N):
            if -11<arr[i][j]<0: # 사람일 때
                dist = abs(ei-i) + abs(ej-j)
                for di,dj in ((-1,0),(1,0),(0,-1),(0,1)):
                    ni, nj = i + di, j + dj
                    # 범위 내, 벽이 아니고, 거리가 가까워지는 곳이면 이동
                    if 0<=ni<N and 0<=nj<N and arr[ni][nj] <= 0 and dist > abs(ei-ni) + abs(ej-nj):
                        narr[i][j] -= arr[i][j] # 이동처리
                        ans += arr[i][j] # 이동거리 합 누적
                        if arr[ni][nj] == -11: # 출구일 떄
                            cnt += arr[i][j] # 탈출
                        else: # 빈칸일 때
                            narr[ni][nj] += arr[i][j] # 이동처리
                        break

    arr = narr
    if cnt == 0: break

    # [2] 미로 회전
    # 한 명 이상의 참가자와 출구를 포함한 가장 작은 정사각형 찾기 / r 좌표 작은 것 우선 / c 좌표 작은 것 우선
    si, sj, L = find_square(arr)

    narr = [x[:] for x in arr]

    # 90도 회전
    for i in range(L):
        for j in range(L):
            narr[si+i][sj+j] = arr[si+L-j-1][sj+i]
            # 벽이면 내구도 1 감소
            if narr[si+i][sj+j] > 0:
                narr[si+i][sj+j] -= 1

    arr = narr
    ei,ej = find_exit(arr)

print(-ans)
print(ei+1,ej+1)