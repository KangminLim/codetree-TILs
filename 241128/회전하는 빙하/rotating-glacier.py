N, Q = map(int,input().split())
N = 2 ** N
arr = [list(map(int,input().split())) for _ in range(N)]
Llst = list(map(int,input().split()))

for q in range(Q):
    narr = [x[:] for x in arr]

    if Llst[q] > 0:
        L = 2 ** (Llst[q])
        HL = 2 ** (Llst[q] - 1)
        for si in range(0,N,L):
            for sj in range(0,N,L):
                for dr in range(4):
                    if dr == 0:
                        for i in range(HL):
                            for j in range(HL):
                                narr[si+i][sj+HL+j] = arr[si+i][sj+j]
                    elif dr == 1:
                        for i in range(HL):
                            for j in range(HL):
                                narr[si+HL+i][sj+HL+j] = arr[si+i][sj+HL+j]
                    elif dr == 2:
                        for i in range(HL):
                            for j in range(HL):
                                narr[si+HL+i][sj+j] = arr[si+HL+i][sj+HL+j]
                    elif dr == 3:
                        for i in range(HL):
                            for j in range(HL):
                                narr[si+i][sj+j] = arr[si+HL+i][sj+j]
        arr = narr

    narr = [x[:] for x in arr]

    for i in range(N):
        for j in range(N):
            if arr[i][j] > 0:
                tmp = 0
                for ni,nj in ((i-1,j),(i,j+1),(i+1,j),(i,j-1)):
                    if 0<=ni<N and 0<=nj<N and arr[ni][nj] > 0:
                        tmp += 1
                if tmp < 3:
                    narr[i][j] -= 1
    arr = narr

from collections import deque
def bfs(si,sj):
    q = deque()
    q.append((si,sj))
    v[si][sj] = True
    cnt = 1
    while q:
        ci,cj = q.popleft()
        for ni,nj in ((ci-1,cj),(ci,cj+1),(ci+1,cj),(ci,cj-1)):
            if 0<=ni<N and 0<=nj<N and not v[ni][nj] and arr[ni][nj] > 0:
                q.append((ni,nj))
                v[ni][nj] = True
                cnt += 1
    return cnt

ans1 = sum(map(sum,arr))
ans2 = 0

v = [[0] * N for _ in range(N)]
for i in range(N):
    for j in range(N):
        if not v[i][j] and arr[i][j] > 0:
            ans2 = max(bfs(i, j),ans2)

print(ans1)
print(ans2)