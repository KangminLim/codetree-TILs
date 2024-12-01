N, M, K = map(int,input().split())
# 참가자 (-1~-9) 출구 (-10)
arr = [list(map(int,input().split())) for _ in range(N)]

for _ in range(M):
    ci,cj = map(lambda x:int(x)-1,input().split())
    arr[ci][cj] -= 1

ei, ej = map(lambda x: int(x) - 1, input().split())
arr[ei][ej] = -10
ans = 0
cnt = M
def find_square(arr):
    mn = N
    for i in range(N):
        for j in range(N):
            if -10 < arr[i][j] < 0:
                mn = min(max(abs(ei-i),abs(ej-j)),mn)

    for si in range(N-mn):
        for sj in range(N-mn):
            if si<=ei<=si+mn and sj<=ej<=sj+mn:
                for i in range(mn+1):
                    for j in range(mn+1):
                        if -10 < arr[si+i][sj+j] < 0:
                            return si,sj,mn+1

def find_exit(arr):
    for i in range(N):
        for j in range(N):
            if arr[i][j] == -10:
                return i,j

for turn in range(1,K+1):

    # 1. 모든 참가자 이동
    narr = [x[:] for x in arr]
    for i in range(N):
        for j in range(N):
            if -10 < arr[i][j] < 0:
                dist = abs(ei-i) + abs(ej-j)
                for ni,nj in ((i-1,j),(i+1,j),(i,j-1),(i,j+1)):
                    if 0<=ni<N and 0<=nj<N and dist > abs(ei-ni) + abs(ej-nj) and arr[ni][nj] <= 0:
                        narr[i][j] -= arr[i][j]
                        ans -= arr[i][j]
                        if (ni,nj) != (ei,ej):
                            narr[ni][nj] += arr[i][j]
                        else:
                            cnt += arr[i][j]
                        break
    if cnt == 0:
        break
    # print('')
    arr = narr
    # 2. 한 명 이상의 참가자와 출구를 포함하는 직사각형 잡기
    si,sj,mn = find_square(arr)
    # print('')

    # 3. 시계 방향 90도 회전, 내구도 -= 1
    narr = [x[:] for x in arr]
    for i in range(mn):
        for j in range(mn):
            narr[si+i][sj+j] = arr[si+mn-1-j][sj+i]
            if narr[si+i][sj+j] > 0:
                narr[si+i][sj+j] -= 1

    # print('')
    arr = narr

    ei,ej = find_exit(arr)
print(ans)
print(ei+1,ej+1)