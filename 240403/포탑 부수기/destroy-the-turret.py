N, M, K = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]
turn = [[0] * M for _ in range(N)] # 공격 턴 계산을 위한 turn

from collections import deque
def laser(si,sj,ei,ej):
    q = deque()
    q.append((si,sj))
    v = [[[] for _ in range(M)] for _ in range(N)] # 방문 경로 확인
    v[si][sj] = (si,sj)
    d = arr[si][sj] # 공격자의 데미지
    while q:
        ci,cj = q.popleft()
        if (ci,cj) == (ei,ej): # 대상까지 접근
            arr[ei][ej] = max(0,arr[ei][ej]-d) # 레이저 공격 d만크
            while True:
                ci,cj = v[ci][cj] # 방문했던 곳 역으로 추적
                if (ci,cj) == (si,sj):
                    return True
                arr[ci][cj] = max(0, arr[ci][cj]) # 경로들은 d//2의 피해
                fset.add((ci,cj))

        for di,dj in ((0,1),(1,0),(0,-1),(-1,0)):
            ni,nj = (ci + di)%N, (cj + dj)%M
            if arr[ni][nj] > 0 and not v[ni][nj]:
                q.append((ni,nj))
                v[ni][nj] = (ci,cj)

    return False

def bomb(si,sj,ei,ej):
    d = arr[si][sj]
    arr[ei][ej] = max(0, arr[ei][ej] - d)
    for di,dj in ((0,-1),(-1,-1),(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1)):
        ni,nj = (ei+di)%N, (ej+dj)%M
        if (si,sj) != (ni,nj):
            arr[ni][nj] = max(0, arr[ni][nj]-d//2)
            fset.add((ni,nj))

# K턴 만큼 시뮬레이션 진행
for T in range(1,K+1):
    # 완전 탐색으로 포탑 탐색 진행
    mn, mx_turn, si, sj = 5001, 0, -1, -1
    # [1] 공격자 선정
    for i in range(N):
        for j in range(M):
            if arr[i][j] <= 0: continue
            if arr[i][j] < mn or (arr[i][j] == mn and mx_turn < turn[i][j]) or \
                (arr[i][j] == mn and mx_turn == turn[i][j] and si+sj < i+j) or \
                (arr[i][j] == mn and mx_turn == turn[i][j] and si+sj == i+j and sj < j):
                mn, mx_turn, si, sj = arr[i][j], turn[i][j], i, j

    # [2] 공격 대상 선정
    mx, mn_turn, ei, ej = -1, 1001, 11, 11
    for i in range(N):
        for j in range(M):
            if arr[i][j] <= 0: continue
            if arr[i][j] > mx or (arr[i][j] == mx and mn_turn > turn[i][j]) or \
                (arr[i][j] == mx and mn_turn == turn[i][j] and si+sj > i+j) or \
                (arr[i][j] == mx and mn_turn == turn[i][j] and si+sj == i+j and sj >j):
                mx, mn_turn, ei, ej = arr[i][j], turn[i][j], i, j

    arr[si][sj] += (N+M) # 공격력 상승
    turn[si][sj] = T # 턴 기록
    fset = set() # 경로를 기록 -> 경로 무관에 쓰임
    fset.add((si,sj))
    fset.add((ei,ej))

    # 레이저 공격 실패하면 -> 포탄 공격
    if laser(si,sj,ei,ej) == False:
        bomb(si,sj,ei,ej)

    for i in range(N):
        for j in range(M):
            if arr[i][j] >0 and (i,j) not in fset: # 부서지지 않고 경로에 무관한 포탑이라면 공격력 1추가
                arr[i][j] += 1

    cnt = N*M
    for lst in arr:
        cnt -= lst.count(0)

    if cnt <=1:
        break

print(max(map(max,arr)))