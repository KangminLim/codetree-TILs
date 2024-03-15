from collections import deque
# 격자 밖
EMPTY = (-1,-1)

n, m = map(int,input().split())
# 0 빈칸, 1 베이스 캠프, 2 아무도 갈 수 없는 곳
mp = [list(map(int,input().split())) for _ in range(n)]
# 편의점 정보
cvs = []

for _ in range(m):
    x, y = map(int,input().split())
    cvs.append((x-1,y-1))
# 사람 초기 값
people = [EMPTY] * m

cur_t = 0

dx = [-1,0,0,1]
dy = [0,-1,1,0]
# 최단 거리
step = [[0] * n for _ in range(n)]
# 방문 표시
visited = [[0] * n for _ in range(n)]

def in_range(x,y):
    return 0<=x<n and 0<=y<n

def can_go(x,y):
    return in_range(x,y) and not visited[x][y] and mp[x][y] != 2
# 시작점으로부터의 최단거리를 구하는 bfs
def bfs(pos):
    # visited, step 값 초기화
    for i in range(n):
        for j in range(n):
            visited[i][j] = False
            step[i][j] = 0

    # 초기 위치 넣기
    q = deque()
    q.append(pos)
    x, y = pos
    visited[x][y] = True
    step[x][y] = 0

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if can_go(nx,ny):
                visited[nx][ny] = True
                step[nx][ny] = step[x][y] + 1
                q.append((nx,ny))

def simulate():
    # step 1. 격자에 있는 사람들에 한하여 편의점 방향을 향해 1칸 이동
    for i in range(m):
        # 격자 밖이나 편의점 도착 인원 패스
        if people[i] == EMPTY or people[i] == cvs[i]:
            continue

        # 편의점 위치를 시작으로 현재 위치까지 오는 최단거리를 구해주는 것이 필요 / 최단거리가 되기 위한 그 다음 위치를 구해야해서
        bfs(cvs[i])

        px,py = people[i]

        # 현재 위치에서 상좌우하 중 최단거리 값이 작은 곳을 고르면 그곳으로 이동하는 것이 최단거리 대로 이동하는 것
        # 그러한 위치 중에서 상좌우하 우선 순위대로 가장 적절한 곳을 고르기
        min_dist = int(1e9)
        min_x, min_y = -1, -1
        for dr in range(4):
            nx, ny = px+dx[dr], py+dy[dr]
            if in_range(nx,ny) and visited[nx][ny] and min_dist > step[nx][ny]:
                min_dist = step[nx][ny]
                min_x, min_y = nx, ny

        people[i] = (min_x, min_y)


    # step 2. 편의점에 도착한 사람에 한하여 grid값 2로 바꾸기
    for i in range(m):
        if people[i] == cvs[i]:
            px,py = people[i]
            mp[px][py] = 2


    # step 3. cur_t <= m 이라면 t번 사람 베이스 캠프로 이동
    if cur_t > m:
        return

    # step 3-1. 편의점으로부터 가장 가까운 베이스 캠프를 고르기 위한 bfs
    bfs(cvs[cur_t-1])

    # step 3-2. 편의점에서 가장 가까운 베이스 캠프 선택 / i, j 증가하는 순으로 돌려서 (행, 열) 우선순위대로
    min_dist = int(1e9)
    min_x, min_y = -1,-1
    for i in range(n):
        for j in range(n):
            if visited[i][j] and mp[i][j] == 1 and min_dist > step[i][j]:
                min_dist = step[i][j]
                min_x, min_y = i, j

    people[cur_t-1] = (min_x, min_y)
    mp[min_x][min_y] = 2

def end():
    for i in range(m):
        if people[i] != cvs[i]:
            return False
    return True

while True:
    cur_t += 1
    simulate()
    if end():
        break
    
print(cur_t)