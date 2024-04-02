N, M, K = map(int,input().split())
arr =[list(map(int,input().split())) for _ in range(N)]

for _ in range(M):
    i, j = map(lambda x:int(x)-1,input().split())
    arr[i][j] -= 1 # 사람 표시

ei, ej = map(lambda x:int(x)-1,input().split())
arr[ei][ej] = -11

def find_square(arr):
    # 한 명 이상의 참가자와 출구를 포함한 가장 작은 정사각형 찾기
    mn = N
    for i in range(N):
        for j in range(N):
            if -11<arr[i][j]<0: # 사람이면
                mn = min(mn, max(abs(ei-i),abs(ej-j))) # 사람이 있을 때 가장 짧은 가로 세로 구하기, min으로 하면 같은 열일 때 0으로 됨)

    # 정사각형 시작 위치 찾기
    for si in range(N-mn):
        for sj in range(N-mn):
            if si <= ei <= si+mn and sj <= ej <= sj+mn: # 정사각형을 완전 탐색해서 출구를 포함하는 정사각형 찾기
                for i in range(si,si+mn+1):
                    for j in range(sj,sj+mn+1):
                        if -11< arr[i][j] < 0: # 사람, 출구 포함 정사각형 시작위치, 길이 리턴
                            return si,sj,mn+1

def find_exit(arr):
    for i in range(N):
        for j in range(N):
            if arr[i][j] == -11:
                return i, j

# K초 동안 시뮬레이션 반복 / cnt = 0이 되면 게임 종료
ans = 0
cnt = M # cnt -> 0이 되면 모두 탈출
for _ in range(K):
    # [1] 모든 인원 한 칸씩 이동
    narr = [x[:] for x in arr] # arr 복사 -> arr에 직접 이동을 해서

    for i in range(N):
        for j in range(N):
            if -11<arr[i][j]<0: # 사람이면
                dist = abs(ei-i) + abs(ej-j)
                for di,dj in ((-1,0),(1,0),(0,-1),(0,1)): # 상하좌우 이동
                    ni, nj = i + di, j + dj
                    # 범위 내, 벽이 아니고, 거리가 가까워 져야한다
                    if 0<=ni<N and 0<=nj<N and arr[ni][nj] <= 0 and dist > abs(ei-ni) + abs(ej-nj):
                        ans += arr[i][j] # 움직인 것은 이동한 걸로 간주하여 더해줌
                        narr[i][j] -= arr[i][j] # 이동 처리
                        if arr[ni][nj] == -11: # 탈출구라면
                            cnt += arr[i][j]
                        else:
                            narr[ni][nj] += arr[i][j] # 이동
                        break

    arr = narr # 변경된 사항 옮기기
    if cnt == 0: break
    # [2] 미로 회전 / 한 명 이상의 참가자와 출구를 포함한 가장 작은 정사각형 잡기
    si, sj, L = find_square(arr)
    narr = [x[:] for x in arr]

    for i in range(L):
        for j in range(L):
            narr[si+i][sj+j] = arr[si+L-j-1][sj+i]
            if narr[si+i][sj+j] > 0: # 내구도 감소
                narr[si+i][sj+j] -= 1

    arr = narr
    # [2-1] 회전된 출구 찾기
    ei,ej = find_exit(arr)

print(-ans)
print(ei+1,ej+1)