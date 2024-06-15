N, M = map(int,input().split())
basecamp = set()
store = {}
arr = [[1] * (N+2)] + [[1] + list(map(int,input().split())) + [1] for _ in range(N)] + [[1] * (N+2)]
for i in range(1,N+1):
    for j in range(1,N+1):
        if arr[i][j] == 1:
            basecamp.add((i,j))
            arr[i][j] = 0

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
            if (ci, cj) in dests:
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
    q = deque()
    arrived = [0] * (M+1)

    while q or time == 1:
        nq = deque()
        alst = []
        # 1. 본인이 가고 싶은 편의점 방향으로 1칸 이동
        for ci,cj,m in q:
            si,sj = store[m]
            ni,nj = find(si,sj,set(((ci-1,cj),(ci,cj-1),(ci,cj+1),(ci+1,cj))))
            if (ni,nj) == store[m]: # 가고싶은 편의점 도착
                alst.append((ni,nj))
                arrived[m] = time
            else:
                nq.append((ni,nj,m))

        q = nq

        # 2. 이동 불가능하게
        if alst:
            for ai,aj in alst:
                arr[ai][aj] = 1

        # 3. time <= m : 자신이 가고 싶은 편의점과 가장 가까이 있는 베이스 컘프에 이동
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