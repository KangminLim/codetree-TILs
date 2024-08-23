N, M, K = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]

for i in range(M):
    ci, cj = map(lambda x:int(x)-1, input().split())
    arr[ci][cj] -= 1 # 사람은 음수 처리

ei,ej = map(lambda x:int(x)-1,input().split())
arr[ei][ej] = -11 # 사람 최대 10명이므로 -11을 출구로 처리
ans = 0
cnt = M
def find_square():
    mn = N
    for i in range(N):
        for j in range(N):
            if -11 < arr[i][j] < 0:
                mn = min(mn, max(abs(ei-i),abs(ej-j)))

    for si in range(N-mn):
        for sj in range(N-mn):
            if si<=ei<=si+mn and sj<=ej<=sj+mn:
                for i in range(mn+1):
                    for j in range(mn+1):
                        if -11< arr[si+i][sj+j] < 0:
                            return si,sj, mn+1

for turn in range(1,K+1):
    # 1. 모든 참가자 이동
    narr = [x[:] for x in arr]
    for i in range(N):
        for j in range(N):
            if -11 < arr[i][j] < 0: # 사람이면
                dist = abs(ei-i) + abs(ej-j)
                # 4방향 이동
                for ni,nj in ((i-1,j),(i+1,j),(i,j-1),(i,j+1)):
                    # 범위 내, 벽이 아니고, 거리가 가까워지는
                    if 0<=ni<N and 0<=nj<N and arr[ni][nj] <= 0 and abs(ei-ni) + abs(ej-nj) < dist:
                        if (ni,nj) == (ei,ej):
                            cnt += arr[i][j]
                            ans -= arr[i][j]
                            narr[i][j] -= arr[i][j]
                            break
                        else:
                            narr[i][j] -= arr[i][j] # 이전 거리 업데이트
                            narr[ni][nj] += arr[i][j] # 이동 위치 업데이트
                            ans -= arr[i][j]
                            break
    if cnt == 0:
        break

    arr = narr
    # 2. 미로 회전
    # 2.1 한 명 이상의 참가자와 출구를 포함한 정사각형 찾기
    si,sj,mn = find_square()

    narr = [x[:] for x in arr]
    # 3. 선택된 미로 회전
    for i in range(mn):
        for j in range(mn):
            narr[si+i][sj+j] = arr[si+mn-1-j][sj+i]
            if narr[si+i][sj+j] > 0:
                narr[si+i][sj+j] -= 1
    arr = narr

    for i in range(N):
        for j in range(N):
            if arr[i][j]==-11:
                ei,ej = i,j


print(ans)
print(ei+1,ej+1)