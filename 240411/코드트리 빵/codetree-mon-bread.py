N, M = map(int,input().split())
# 벽으로 둘러싸기
arr = [[1] * (N+2)] + [[1] + list(map(int,input().split())) + [1] for _ in range(N)] + [[1] * (N+2)]

# 베이스 캠프 처리
basecamp = set()

for i in range(1,N+1):
    for j in range(1,N+1):
        if arr[i][j] == 1:
            basecamp.add((i,j))
            arr[i][j] = 0

store = {}

for idx in range(1,M+1):
    i,j = map(int,input().split())
    store[idx] = (i,j)

from collections import deque

def find(si,sj,dests):
    q = deque()
    q.append((si,sj))
    v = [[False] * (N+2) for _ in range(N+2)]
    v[si][sj] = True
    tlst = []
    while q:
        nq = deque()
        for ci,cj in q:

            if (ci,cj) in dests: # 목적지 도착
                tlst.append((ci,cj))

            else:
                for ni,nj in ((ci-1,cj),(ci,cj-1),(ci,cj+1),(ci+1,cj)):
                    if arr[ni][nj] == 0 and not v[ni][nj]:
                        nq.append((ni,nj))
                        v[ni][nj] = True
        q = nq

        if tlst:
            return sorted(tlst)[0]

def solve():
    time = 1
    arrived = [0] * (M+1)
    q = deque()

    while q or time == 1:
        nq = deque()
        tlst = []
        # [1] 격자에 있는 사람들 모두가 본인이 가고 싶은 편의점 방향을 향해 1칸 움직임 (상우하좌)
        for ci,cj,m in q:
            if arrived[m] == 0:
                ni,nj = find(store[m][0],store[m][1],set(((ci-1,cj),(ci,cj+1),(ci+1,cj),(ci,cj-1))))
                if (ni,nj) == store[m]:
                    tlst.append((ni,nj))
                    arrived[m] = time
                else:
                    nq.append((ni,nj,m))
        q = nq

        # [2] 편의점에 도착했으면 더이상 지나갈 수 없게 만들기
        if tlst:
            for ti, tj in tlst:
                arr[ti][tj] = 1

        # [3] time<=M이라면 자신이가 가고 싶은 편의점으로 이동
        if time <= M:
            si,sj = store[time]
            ei,ej = find(si,sj,basecamp)
            basecamp.remove((ei,ej))
            arr[ei][ej] = 1
            q.append((ei,ej,time))

        time += 1

    return max(arrived)

ans = solve()
print(ans)