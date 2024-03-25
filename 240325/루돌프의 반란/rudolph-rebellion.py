def in_range(x,y):
    return 1<=x<=n and 1<=y<=n

n,m,p,c,d = map(int,input().split())
rudolf = tuple(map(int,input().split()))

points = [0 for _ in range(p+1)]
pos = [(0,0) for _ in range(p+1)]
board = [[0 for _ in range(n+1)] for _ in range(n+1)]
is_live = [False for _ in range(p+1)]
stun = [0 for _ in range(p+1)]

dx = [-1, 0, 1,0]
dy = [0, 1, 0, -1]

board[rudolf[0]][rudolf[1]] = -1

for _ in range(p):
    id, x, y = tuple(map(int,input().split()))
    pos[id] = (x,y)
    board[pos[id][0]][pos[id][1]] = id
    is_live[id] = True

for t in range(1,m+1):
    closestX, closestY, closestIdx = 10000, 10000, 0

    # 살아있는 루돌프 중 루돌프에 가장 가까운 산타를 찾습니다.
    for i in range(1, p+1):
        if not is_live[i]:
            continue

        currentBest = ((closestX-rudolf[0]) ** 2 + (closestY-rudolf[1]) ** 2, (-closestX, -closestY))
        currentValue = ((pos[i][0] - rudolf[0]) ** 2 + (pos[i][1] - rudolf[1]) ** 2, (-pos[i][0], -pos[i][1]))

        if currentValue < currentBest:
            closestX, closestY = pos[i]
            closestIdx = i

    # 가장 가까운 산타의 방향으로 루돌프가 이동
    if closestIdx:
        prevRudolf = rudolf
        moveX = 0
        if closestX > rudolf[0]:
            moveX = 1
        elif closestX < rudolf[0]:
            moveX = -1

        moveY = 0
        if closestY > rudolf[1]:
            moveY = 1
        elif closestY < rudolf[1]:
            moveY = -1

        rudolf = (rudolf[0] + moveX, rudolf[1] + moveY)
        board[prevRudolf[0]][prevRudolf[1]] = 0

    # 루돌프의 이동으로 충돌한 경우, 산타를 이동시키고 처리를 합니다.
    if rudolf[0] == closestX and rudolf[1] == closestY:
        firstX = closestX + moveX * c
        firstY = closestY + moveY * c
        lastX, lastY = firstX, firstY

        stun[closestIdx] = t + 1

        # 연쇄 이동
        while in_range(lastX,lastY) and board[lastX][lastY] > 0:
            lastX += moveX
            lastY += moveY

        # while not (lastX == firstX and lastY == firstY):
        #     beforeX = lastX - moveX
        #     beforeY = lastY - moveY
        #
        #     if not in_range(beforeX,beforeY):
        #         break
        #
        #     idx = board[beforeX][beforeY]
        #
        #     if not in_range(beforeX,beforeY):
        #         is_live[idx] = False
        #     else:
        #         board[lastX][lastY] = board[beforeX][beforeY]
        #         pos[idx] = (lastX, lastY)
        #
        #     lastX, lastY = beforeX, beforeY

        points[closestIdx] += c
        pos[closestIdx] = (firstX,firstY)
        if in_range(firstX,firstY):
            board[firstX][firstY] = closestIdx
        else:
            is_live[closestIdx] = False

    board[rudolf[0]][rudolf[1]] = -1

    # 산타의 이동
    for i in range(1,p+1):
        if not is_live[i] or stun[i] >= t:
            continue

        minDist = (pos[i][0] - rudolf[0]) ** 2 + (pos[i][1] - rudolf[1]) ** 2
        moveDir = -1

        for dir in range(4):
            nx = pos[i][0] + dx[dir]
            ny = pos[i][1] + dy[dir]

            if not in_range(nx,ny) or board[nx][ny] > 0:
                continue

            dist = (nx - rudolf[0]) ** 2 + (ny-rudolf[1]) ** 2

            if dist < minDist:
                minDist = dist
                moveDir = dir

        if moveDir != -1:
            nx = pos[i][0] + dx[moveDir]
            ny = pos[i][1] + dy[moveDir]

            # 산타의 이동으로 충돌
            if nx == rudolf[0] and ny == rudolf[1]:
                stun[i] = t+1

                moveX = -dx[moveDir]
                moveY = -dy[moveDir]

                firstX = nx + moveX * d
                firstY = ny + moveY * d
                lastX, lastY = firstX, firstY

                if d==1:
                    points[i] += d
                else:

                    while in_range(lastX,lastY) and board[lastX][lastY] > 0:
                        lastX += moveX
                        lastY += moveY

                    while lastX != firstX or lastY != firstY:
                        beforeX = lastX - moveX
                        beforeY = lastY - moveY

                        if not in_range(beforeX,beforeY):
                            break

                        idx = board[beforeX][beforeY]

                        if not in_range(lastX,lastY):
                            is_live[idx] = False
                        else:
                            board[lastX][lastY] = board[beforeX][beforeY]
                            pos[idx] = (lastX, lastY)

                        lastX,lastY = beforeX, beforeY

                    points[i] += d
                    board[pos[i][0]][pos[i][1]] = 0
                    pos[i] = (firstX, firstY)
                    if in_range(firstX,firstY):
                        board[firstX][firstY] = i
                    else:
                        is_live[i] = False

            else:
                board[pos[i][0]][pos[i][1]] = 0
                pos[i] = (nx,ny)
                board[nx][ny] = i

    for i in range(1,p+1):
        if is_live[i]:
            points[i] += 1
# 결과를 출력
for i in range(1,p+1):
    print(points[i], end=' ')