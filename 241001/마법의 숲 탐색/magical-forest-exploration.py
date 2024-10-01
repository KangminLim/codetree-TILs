R, C, K = map(int,input().split())

di,dj = [-1,0,1,0],[0,1,0,-1]

arr = [[-1]+ [0] * C + [-1] for _ in range(R+3)] + [[-1] * (C+2)]

Exit = [[0] * (C + 2) for _ in range(R + 4)]

ans = 0
from collections import deque
def bfs(si,sj):
    q = deque()
    q.append((si,sj))
    v = [[False] * (C+2) for _ in range(R + 4)]
    v[si][sj] = True
    mx = 0
    while q:
        ci,cj = q.popleft()
        for ni,nj in ((ci-1,cj),(ci,cj+1),(ci+1,cj),(ci,cj-1)):
            # if 3<=ni<R+3 and 0<=nj<C and not v[ni][nj] and ((arr[si][sj] == arr[ni][nj]) or (Exit[ci][cj] and arr[ci][cj] != arr[ni][nj])):
            if arr[ni][nj] > 0 and not v[ni][nj] and ((arr[ci][cj] == arr[ni][nj]) or (Exit[ci][cj] and arr[ci][cj] != arr[ni][nj])):
                q.append((ni,nj))
                v[ni][nj] = True
                if ni > mx:
                    mx = ni
    return mx-2


for idx in range(1,K+1):
    cj, dr = map(int, input().split())
    ci = 1

    while True:
        # 1. 남쪽 칸 이동 가능
        # if (1<=ci<R+1 and 1<=cj<C-1):
        if arr[ci+1][cj-1] == 0 and arr[ci+2][cj] == 0 and arr[ci+1][cj+1] == 0:
            ci += 1
        # 2. 서쪽 회전 가능
        elif arr[ci-1][cj-1] == 0 and arr[ci][cj-2] == 0 and arr[ci+1][cj-1] == 0 and arr[ci+1][cj-2] == 0 and arr[ci+2][cj-1] == 0:
            ci += 1
            cj -= 1
            dr = (dr-1)%4
        # 3. 동쪽 회전 가능
        elif arr[ci-1][cj+1] == 0 and arr[ci][cj+2] == 0 and arr[ci+1][cj+1] == 0 and arr[ci+1][cj+2] == 0 and arr[ci+2][cj+1] == 0:
            ci += 1
            cj += 1
            dr = (dr+1)%4
        # 4. 정령이 갈 수 있는 가장 남쪽 도착
        else:
            break
        # print('')
        # else:
        #     break
        # print('')

    if ci < 4:
        # arr = [[0] * C for _ in range(R + 3)]
        arr = [[-1] + [0] * C + [-1] for _ in range(R + 3)] + [[-1] * (C+2)]
        Exit = [[False] * (C+2) for _ in range(R + 4)]
        # Exit = [[0] * C for _ in range(R + 3)]
        continue
    else:
        for k in range(4):
            ni,nj = ci+di[k], cj+dj[k]
            arr[ni][nj] = idx
        arr[ci][cj] = idx
        Exit[ci+di[dr]][cj+dj[dr]] = True
        tmp = bfs(ci,cj)
        ans += tmp
    # print('')

print(ans)