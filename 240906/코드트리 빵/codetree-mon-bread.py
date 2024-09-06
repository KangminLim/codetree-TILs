N, M = map(int,input().split())
arr = [[1] * (N+2)] + [[1] + list(map(int,input().split())) + [1] for _ in range(N)] + [[1] * (N+2)]
basecamp = set()
for i in range(1,N+1):
    for j in range(1,N+1):
        if arr[i][j] == 1:
            basecamp.add((i,j))
            arr[i][j] = 0
store = {}
for idx in range(1,M+1):
    ci,cj = map(int,input().split())
    store[idx] = (ci,cj)

time = 1
arrived = [0] * (M+1)
from collections import deque
def find(si,sj,dest):
    q = deque()
    q.append((si,sj))
    v = [[False] * (N+2) for _ in range(N+2)]
    v[si][sj] = True
    tlst = []
    while q:
        nq = deque()
        for ci,cj in q:
            if (ci, cj) in dest:
                tlst.append((ci,cj))
            else:
                for ni,nj in ((ci-1,cj),(ci,cj-1),(ci,cj+1),(ci+1,cj)):
                    if arr[ni][nj] == 0 and not v[ni][nj]:
                        nq.append((ni,nj))
                        v[ni][nj] = True
        q = nq

        if tlst:
            return sorted(tlst)[0]

q = []
while time == 1 or q:
    # 1. 격자에 있다면 본인이 가고싶은 편의점 방향으로 이동
    nq = []
    tlst = []
    for ci,cj,m in q:
        ni,nj = find(store[m][0],store[m][1],set(((ci-1,cj),(ci,cj-1),(ci,cj+1),(ci+1,cj))))
        if (ni,nj) == store[m]:
            arrived[m] = time
            tlst.append((ni,nj))
        else:
            nq.append((ni,nj,m))
    q = nq
    # 2. 이동불가 처리
    if tlst:
        for ti,tj in tlst:
            arr[ti][tj] = 1

    # 3. 베이스 캠프 처리
    if time <= M:
        si,sj = store[time]
        ei,ej = find(si,sj,basecamp)
        basecamp.remove((ei,ej))
        arr[ei][ej] = 1
        q.append((ei,ej,time))

    time += 1

print(max(arrived))