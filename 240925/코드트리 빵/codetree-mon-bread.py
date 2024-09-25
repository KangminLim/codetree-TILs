N, M = map(int,input().split())
arr = [[1] * (N+2)] + [[1] + list(map(int,input().split())) + [1] for _ in range(N)] + [[1] * (N+2)]
store = {}
basecamp = set()

from collections import deque

for i in range(1,N+1):
    for j in range(1,N+1):
        if arr[i][j] == 1:
            basecamp.add((i,j))
            arr[i][j] = 0

for idx in range(1,M+1):
    si, sj = map(int,input().split())
    store[idx] = (si,sj)

q = deque()
time = 1
arrived = [0] * (N+1)

def find(si,sj,dest):
    q = deque()
    q.append((si,sj))
    v = [[0] * (N+2) for _ in range(N+2)]
    v[si][sj] = True
    tlst = []
    while q:
        nq = deque()
        for ci,cj in q:
            if (ci, cj) in dest:
                tlst.append((ci, cj))
            else:
                for ni,nj in ((ci-1,cj),(ci+1,cj),(ci,cj-1),(ci,cj+1)):
                    if not v[ni][nj] and arr[ni][nj] == 0:
                        nq.append((ni,nj))
                        v[ni][nj] = True
        if tlst:
            return sorted(tlst)[0]

        q = nq

while time == 1 or q:
    nq = deque()
    tlst = []
    # 1. 본인이 가고싶은 편의점으로 이동
    for ci,cj,m in q:
        ni,nj = find(store[m][0], store[m][1], set(((ci-1,cj),(ci+1,cj),(ci,cj-1),(ci,cj+1))))
        if (ni,nj) == store[m]:
            tlst.append((ni,nj))
            arrived[m] = time
        else:
            nq.append((ni,nj,m))

    q = nq
    # 2. 편의점 도착한 사람 이동 불가 처리
    if tlst:
        for ti,tj in tlst:
            arr[ti][tj] = 1

    # 3. 베이스 캠프 이동
    if time <= M:
        si,sj = store[time]
        ei,ej = find(si,sj,basecamp)
        arr[ei][ej] = 1
        basecamp.remove((ei,ej))
        q.append((ei,ej,time))
    time += 1

print(max(arrived))