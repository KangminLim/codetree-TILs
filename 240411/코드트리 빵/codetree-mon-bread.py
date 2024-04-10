N, M = map(int,input().split())
arr = [[1] * (N+2)] + [[1] + list(map(int,input().split())) + [1] for _ in range(N)] + [[1] * (N+2)]

basecamp = set()

for i in range(1,N+1):
    for j in range(1,N+1):
        if arr[i][j] == 1:
            basecamp.add((i,j))
            arr[i][j] = 0

store = {}
for m in range(1,M+1):
    i,j = map(int,input().split())
    store[m] = (i,j)


from collections import deque
def find(si,sj,dests):
    q = deque()
    q.append((si,sj))
    v = [[False] * (N+2) for _ in range(N+2)]
    v[si][sj] = True
    alst = []
    while q:
        nq = deque()
        for ci, cj in q:

            if (ci,cj) in dests:
                alst.append((ci,cj))

            else:
                for ni,nj in ((ci-1,cj),(ci+1,cj),(ci,cj-1),(ci,cj+1)):
                    if arr[ni][nj] == 0 and not v[ni][nj]:
                        nq.append((ni,nj))
                        v[ni][nj] = True
        q = nq

        if alst:
            return sorted(alst)[0]



def solve():
    q = deque()
    time = 1
    arrived = [0] * (M+1)
    while q or time == 1:
        nq = deque()
        tlst = []
        # [1] 격자에 있는 사람들 모두가 본인이 가고 싶은 편의점 방향을 향해서 1칸 움직이기
        for ci,cj,m in q:
            if arrived[m] == 0:
                ni, nj = find(store[m][0], store[m][1], set(((ci - 1, cj), (ci + 1, cj), (ci, cj - 1), (ci, cj + 1))))
                if (ni,nj) == store[m]:
                    tlst.append((ni,nj))
                    arrived[m] = time
                else:
                    if arr[ni][nj] == 0:
                        nq.append((ni,nj,m))

        q = nq
        # [2] 편의점에 도착하면 해당 편의점 이동 불가 처리
        if tlst:
            for ai,aj in tlst:
                arr[ai][aj] = 1


        # [3] 본인 편의점에서 가장 가까운 베이스 캠프
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