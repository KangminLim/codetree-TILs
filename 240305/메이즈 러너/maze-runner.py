n,m,k = tuple(map(int,input().split()))

# 모든 벽의 상태 기록
board = [[0] * (n+1) for _ in range(n+1)]
for i in range(1,n+1):
    board[i] = [0] + list(map(int,input().split()))

next_board = [[0] * (n+1) for _ in range(n+1)]

# 참가자의 위치 정보를 기록
runner = [(-1,-1)] + [tuple(map(int,input().split())) for _ in range(m)]

# 출구의 위치 정보를 기록
exits = tuple(map(int,input().split()))

ans = 0

# 회전해야 하는 최소 정사각형을 찾아 기록
sx, sy, square_size = 0, 0, 0

# 1. 이동함수 정의
def move_all_runner():
    global exits, ans

    # 1.1 모든 참가자에 대해 이동 진행
    for i in range(1, m+1):
        # 1.1.1 이미 출구에 있으면 스킵
        if runner[i] == exits:
            continue
        tx, ty = runner[i]
        ex, ey = exits

        # 1.1.2 행이 다른 경우 행을 이동 (우선순위 행>열)
        if tx != ex:
            nx, ny = tx, ty
            if ex > nx:
                nx += 1
            else:
                nx -= 1

            # 벽이 없다면 행 이동 / 이동 후 다음 참가자로 넘어감
            if board[nx][ny] == 0:
                runner[i] = (nx,ny)
                ans += 1
                continue

        # 1.1.3 열이 다른 경우 열을 이동
        if ty != ey:
            nx, ny = tx, ty

            if ey > ny:
                ny += 1
            else:
                ny -= 1

            if board[nx][ny] == 0:
                runner[i] = (nx,ny)
                ans += 1
                continue

# 2. 미로 선정 함수
def find_minimum_square():
    global exits, sx, sy, square_size
    ex, ey = exits

    # 2.1 3중 for문
    for sz in range(2,n+1):
        for x1 in range(1,n-sz+2):
            for y1 in range(1,n-sz+2):
                x2, y2 = x1 + sz - 1, y1 + sz - 1
                # 2.1.1 출구가 정사각형안에 없다면 continue
                if not(x1<=ex<=x2 and y1<=ey<=y2):
                    continue

                is_runner_in = False
                # 2.1.2 참가자가 안에 있는지 판단
                for l in range(1,m+1):
                    tx, ty = runner[l]
                    if x1 <= tx <= x2 and y1 <= ty <= y2:
                        if not (tx == ex and ty == ey):
                            is_runner_in = True
                # 2.1.3 sx, sy, square_size 갱신
                if is_runner_in:
                    sx = x1
                    sy = y1
                    square_size = sz
                    return

# 3. 벽 회전 함수
def rotate_square():
    # 3.1 내구도 감소
    for x in range(sx, sx+square_size):
        for y in range(sy, sy+square_size):
            if board[x][y]:
                board[x][y] -= 1
    # 3.2 회전
    for x in range(sx, sx+square_size):
        for y in range(sy,sy+square_size):
            # step 1. (sx,sy)를 (0,0)으로 올겨주는 변환을 진행
            ox, oy = x - sx, y - sy
            # step 2. 변환된 상태에서는 회전 이후의 좌표가 (x, y), (y, square_n-x-1)가 된다.
            rx, ry = oy, square_size-ox-1
            # step 3. 다시 (sx, sy)를 더해준다.
            next_board[rx+sx][ry+sy] = board[x][y]
    # next_board 값을 현재 board에 옮기기.
    for x in range(sx, sx+square_size):
        for y in range(sy, sy+square_size):
            board[x][y] = next_board[x][y]

# 4. 모든 참가자 및 출구 회전 함수
def rotate_runner_and_exit():
    global exits

    # 4.1 모든 참가자 회전
    for i in range(1,m+1):
        tx,ty = runner[i]

        if sx <= tx < sx+square_size and sy<=ty<sy+square_size:
            # step 1. (sx,sy)를 (0,0)으로 옮겨주는 변환을 진행
            ox, oy = tx - sx, ty - sy
            # step 2. 변환된 상태에서는 회전 이후의 좌표가 (x,y), (y, square_n-x-1)가 된다.
            rx, ry = oy, square_size-ox-1
            # step 3. 다시 (sx, sy)를 더해준다.
            runner[i] = (rx+sx, ry+sy)

    # 4.2 출구 회전
    ex, ey = exits
    if sx <= ex < sx + square_size and sy <= ey < sy + square_size:
        # step 1. (sx, sy)를 (0,0)으로 옮겨주는 변환을 진행
        ox, oy = ex - sx, ey - sy
        # step 2. (변환된 상태에서는 회전 이후의 좌표가 (x,y), (y, square_n-x-1)가 된다.
        rx, ry = oy, square_size-ox-1
        # step 3. 다시 (sx,sy)를 더해준다.
        exits = (rx+sx, ry+sy)

# 5. for문 range(k)
for _ in range(k):
    # 5.1 모든 참가자 이동
    move_all_runner()

    # 5.2 모든 사람이 출구로 탈출했는지 판단
    is_all_escaped = True
    for i in range(1,m+1):
        if runner[i] != exits:
            is_all_escaped = False

    # 만약 모든 사람이 출구로 탈출했으면 바로 종료
    if is_all_escaped:
        break

    # 5.3 한 명 이상의 참가자와 출구를 포함한 가장 작은 정사각형을 찾는다.
    find_minimum_square()

    # 5.4 정사각형 내부의 벽 회전
    rotate_square()

    # 5.5 모든 참가자와 출구를 회전
    rotate_runner_and_exit()

print(ans)

ex, ey = exits
print(ex,ey)