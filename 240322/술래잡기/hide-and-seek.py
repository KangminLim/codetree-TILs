n,m,h,k = map(int,input().split())
dx = [-1,0,1,0]
dy = [0,1,0,-1]
# 맵
graph = [[0] * (n+1) for _ in range(n+1)]
# 술래 (상 방향부터 시작)
seeker = [((n+1)//2,(n+1)//2),0]
#mx_cnt, cnt, flag, val
seeker_snail = [1, 0, 0, 1]
# 도망자
hider = [[(-1,-1),-1,-1]] * (m+1)
# 생존 여부
is_lived = [True] * (m+1)
# 도망자 정보
for i in range(1,m+1):
    x,y,d = map(int,input().split())
    hider[i] = [(x,y),d,-1]
# 그래프에 나무 추가
for i in range(h):
    x,y = map(int,input().split())
    graph[x][y] = 1
answer = 0
# 최단거리 구하기
def distance(idx,hider,seeker):
    hx,hy = hider[idx][0][0], hider[idx][0][1]
    mx,my = seeker[0][0],seeker[0][1]
    dist = abs(hx-mx) + abs(hy-my)
    if dist <= 3:
        return True
    else:
        return False
# 범위 구하기
def in_range(x,y):
    return 0<x<=n and 0<y<=n

def direction(d,dr):
    # dr 초기값 선정
    if dr == -1:
        if d == 1:
            dr = 1
            return dr
        else:
            dr = 2
            return dr
    # 초기가 아닐 때
    else:
        # 좌우일 떄
        if d == 1:
            if dr == 1:
                dr += 2

            else:
                dr -= 2
        # 상하일 때
        elif d == 2:
            if dr == 0:
                dr += 2
            else:
                dr -= 2
    return dr

def hider_move():
    global hider
    for i in range(1,m+1):
        # 최단 거리 및 생존 여부 판단
        if not distance(i,hider,seeker) and not is_lived[i]:
           continue
        # x,y,(좌우,상하),현재 dr
        x,y,d,dr = hider[i][0][0],hider[i][0][1], hider[i][1], hider[i][2]

        # dr 초기값 선정
        if dr == -1:
            dr = direction(d,dr)

        nx,ny = x+dx[dr],y+dy[dr]
        # 격자 범위 벗어나지 않음
        if in_range(nx,ny):
            # 방향 변경 없고, 이동 안하고 종료
            if (nx,ny) == (seeker[0][0], seeker[0][1]):
                continue
            # 이동
            else:
                # hider 움직임 좌표 반영, 위치 반영
                hider[i][0] = (nx, ny)
                hider[i][2] = dr
        # 격자 범위 벗어남
        else:
            dr = direction(d,dr)
            nx, ny = x + dx[dr], y + dy[dr]
            if in_range(nx, ny):
                # 방향 변경 하고, 이동 안하고 종료
                if (nx, ny) == (seeker[0][0], seeker[0][1]):
                    hider[i][2] = dr

                else:
                    # hider 움직임 좌표 반영
                    hider[i][0] = (nx, ny)
                    hider[i][2] = dr


def seeker_move():
    global seeker, seeker_snail
    sx, sy, dr = seeker[0][0],seeker[0][1],seeker[1]
    mx_cnt, cnt, flag, val = seeker_snail
    cnt += 1

    nx,ny = sx+dx[dr], sy+dy[dr]
    # 끝점 도착하면 중앙으로
    if (nx, ny) == (1, 1):
        mx_cnt, cnt, flag, val = n, 1, 1, -1
        dr = 2

    elif (nx,ny) == (n//2,n//2):
        mx_cnt,cnt,flag,val = 1,0,0,1
        dr = 0

    # 방향 변경
    else:
        if cnt == mx_cnt:
            cnt = 0
            dr = (dr+val) % 4
            if flag == 0:
                flag = 1
            # 두 번에 한번씩 길이 증가
            else:
                flag = 0
                mx_cnt += val

    # update
    seeker[0],seeker[1] = (nx,ny),dr
    seeker_snail = mx_cnt,cnt,flag,val

def seeker_seek(t):
    global seeker, hider, answer
    sx, sy, dr = seeker[0][0],seeker[0][1],seeker[1]
    for dist in range(3):
        nx, ny = sx + dist * dx[dr], sy + dist * dy[dr]
        if in_range(nx,ny):
           if graph[nx][ny] == 0:
                for i in range(1,m+1):
                    x, y = hider[i][0]
                    if (nx,ny) == (x,y) and is_lived[i]:
                        answer += t
                        is_lived[i] = False

for t in range(1,k+1):
    hider_move()
    seeker_move()
    seeker_seek(t)
print(answer)