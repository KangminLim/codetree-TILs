from collections import deque

MAX_N = 31
MAX_L = 41
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

mp = [[0 for _ in range(MAX_L)] for _ in range(MAX_L)]
bef_k = [0 for _ in range(MAX_N)]
knight = [[0,0,0,0,0] for _ in range(MAX_N)]
n_pos = [[0,0] for _ in range(MAX_N)]
dmg = [0 for _ in range(MAX_N)]
visited = [False for _ in range(MAX_N)]

def try_movement(idx, dr):
    q = deque()

    # 초기화 작업
    for i in range(1,n+1):
        dmg[i] = 0
        visited[i] = False
        n_pos[i][0] = knight[i][0]
        n_pos[i][1] = knight[i][1]

    q.append(idx)
    visited[idx] = True

    while q:
        # 왕의 명령 idx 넣기
        x = q.popleft()

        n_pos[x][0] += dx[dr]
        n_pos[x][1] += dy[dr]

        # 범위 체크
        if n_pos[x][0] < 1 or n_pos[x][1] < 1 or n_pos[x][0] + knight[x][2] -1 > l or n_pos[x][1] + knight[x][3] - 1 > l:
            return False

        for i in range(n_pos[x][0], n_pos[x][0] + knight[x][2]):
            for j in range(n_pos[x][1], n_pos[x][1] + knight[x][3]):
                if mp[i][j] == 1:
                    dmg[x] += 1
                if mp[i][j] == 2:
                    return False

        for i in range(1, n+1):
            if visited[i] or knight[i][4] <= 0:
                continue
            if knight[i][0] > n_pos[x][0] + knight[x][2] - 1 or n_pos[x][0] > knight[i][0] + knight[i][2] - 1:
                continue
            if knight[i][1] > n_pos[x][1] + knight[x][2] - 1 or n_pos[x][1] > knight[i][1] + knight[i][3] - 1:
                continue

            visited[i] = True
            q.append(i)

    dmg[idx] = 0
    return True

def move_knight(idx, dr):
    if knight[idx][4] <= 0:
        return
    if try_movement(idx,dr):
        for i in range(1,n+1):
            knight[i][0] = n_pos[i][0]
            knight[i][1] = n_pos[i][1]
            knight[i][4] -= dmg[i]

l, n, q = map(int,input().split())
for i in range(1,l+1):
    mp[i][1:] = map(int,input().split())
for i in range(1,n+1):
    # r,c,h,w,k
    knight[i][0],knight[i][1],knight[i][2],knight[i][3],knight[i][4] = map(int,input().split())
    bef_k[i] = knight[i][4]

for _ in range(q):
    idx, dr = map(int,input().split())
    move_knight(idx,dr)

ans = sum([bef_k[i] - knight[i][4] for i in range(1,n+1) if knight[i][4] >0])
print(ans)