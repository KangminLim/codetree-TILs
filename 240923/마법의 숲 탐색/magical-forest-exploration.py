R, C, K = map(int,input().split())
arr = [[0] * C for _ in range(R+3)]
exit = [[0] * C for _ in range(R+3)]
di,dj = [-1,0,1,0],[0,1,0,-1]
ans = 0

from collections import deque
def bfs(si,sj):
    q = deque()
    q.append((si,sj))
    v = [[0] * C for _ in range(R + 3)]
    v[si][sj] = True
    mx = 0
    while q:
        ci,cj = q.popleft()
        for ni,nj in ((ci-1,cj),(ci,cj+1),(ci+1,cj),(ci,cj-1)):
            if 0<= ni < R+3 and 0<= nj< C and not v[ni][nj] and arr[ni][nj] > 0 and ((arr[ni][nj] == arr[ci][cj]) or ((arr[ni][nj] != arr[ci][cj]) and exit[ci][cj])):
                q.append((ni,nj))
                v[ni][nj] = True
                mx = max(ni,mx)
    return mx-2

for idx in range(1,K+1):
    cj, cd = map(int,input().split())
    cj -= 1
    ci = 1
    while True:
        # 1. 앞부분이 빈칸이면 남쪽 이동
        sflag = True
        lflag = True
        llflag = True
        rflag = True
        rrflag = True
        for ni,nj in ((ci+1,cj-1),(ci+2,cj),(ci+1,cj+1)):
            if 0<=ni<R+3 and 0<=nj<C and not arr[ni][nj]:
                continue
            else:
                sflag = False

        if sflag:
            ci += 1
            continue

        else:
            for ni, nj in ((ci-1,cj-1),(ci,cj-2),(ci+1,cj-1),(ci+2,cj-1),(ci+1,cj-2)):
                if 0 <= ni < R + 3 and 0 <= nj < C and not arr[ni][nj]:
                    continue
                else:
                    lflag = False

            if lflag:
                cj -= 1
                ci += 1
                cd = (cd-1)%4
                continue

            else:
                for ni, nj in ((ci - 1, cj + 1), (ci, cj + 2), (ci + 1, cj + 1), (ci + 2, cj + 1),(ci + 1, cj+2)):
                    if 0 <= ni < R + 3 and 0 <= nj < C and not arr[ni][nj]:
                        continue
                    else:
                        rflag = False


                if rflag:
                    ci += 1
                    cj += 1
                    cd = (cd+1)%4
                    continue


                if not sflag and not rflag and not lflag:
                    if ci <=2:
                        arr = [[0] * C for _ in range(R + 3)]
                        exit = [[0] * C for _ in range(R + 3)]
                        break

                    for ni, nj in ((ci - 1, cj), (ci, cj), (ci, cj - 1), (ci, cj + 1), (ci + 1, cj)):
                        arr[ni][nj] = idx
                        eflag = False
                    ei,ej = ci+di[cd], cj+dj[cd]
                    exit[ei][ej] = True
                    tmp = bfs(ci,cj)
                    ans += tmp
                if not eflag:
                    break

print(ans)