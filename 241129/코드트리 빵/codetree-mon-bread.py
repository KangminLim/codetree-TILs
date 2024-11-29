N, M = map(int,input().split())
arr = [[1] * (N+2)] + [[1] + list(map(int,input().split())) + [1] for _ in range(N)] + [[1] * (N+2)]
basecamp = set()
store = {}

for i in range(1,N+1):
    for j in range(1,N+1):
        if arr[i][j] == 1:
            basecamp.add((i,j))
            arr[i][j] = 0

for i in range(1,M+1):
    ci,cj = map(int,input().split())
    store[i] = (ci,cj)

from collections import deque
def find(si,sj,dest):
    q = deque()
    q.append((si,sj))
    v = [[False] * (N+2) for _ in range(N+2)]
    v[si][sj] = True

    while q:
        nq = deque()
        tlst = []

        for ci,cj in q:
            if (ci,cj) in dest:
                tlst.append((ci,cj))
            else:
                for ni,nj in ((ci-1,cj),(ci,cj-1),(ci,cj+1),(ci+1,cj)):
                    if arr[ni][nj] == 0 and not v[ni][nj]:
                        v[ni][nj] = True
                        nq.append((ni,nj))
        if tlst:
            return sorted(tlst,key=lambda x:(x[0],x[1]))[0]
        q = nq


time = 1
arrived = [0] * (M+1)
q = deque()

while time == 1 or q:
    nq = deque()
    tlst = []

    # 1. 사람 이동
    for ci, cj, m in q:
        ni, nj = find(store[m][0], store[m][1], set(((ci - 1, cj), (ci, cj - 1), (ci, cj + 1), (ci + 1, cj))))
        if (ni,nj) == store[m]:
            arrived[m] = time
            tlst.append((ni,nj))
        else:
            nq.append((ni,nj,m))
    q = nq
    # 2. 이동 불가 처리
    if tlst:
        for ti, tj in tlst:
            arr[ti][tj] = 1

    # 3. 베이스 캠프 이동
    if time <= M:
        ni,nj = find(store[time][0],store[time][1],basecamp)
        basecamp.remove((ni,nj))
        arr[ni][nj] = 1
        q.append((ni,nj,time))
    time += 1

print(max(arrived))