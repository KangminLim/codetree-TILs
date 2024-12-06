from collections import deque
import copy

def isInBoard(r,c):
    return (0<=r<N and 0<=c<N)

#목적지 도달 가능 경로 뽑기
def bfs(r,c, fR,fC):
    visited = [[0]*N for _ in range(N)]
    visited[r][c]=1
    q = deque()
    q.append((r,c))
    tmpp = []
    while q:
        r,c = q.popleft()
        if (r,c)==(fR, fC):
            tR,tC = eR,eC
            stR, stC = sR,sC
            while True:
                tmpp.append((tR,tC))
                if (tR,tC) == (stR,stC):
                    break
                tR, tC = visited[tR][tC]
        for dr, dc in [(-1,0),(1,0),(0,-1),(0,1)]:
            nr,nc = r+dr,c+dc
            if not isInBoard(nr,nc):
                continue
            if BoardArr[nr][nc]==0 and visited[nr][nc]==0:
                visited[nr][nc]=(r,c)
                q.append((nr,nc))

    return tmpp

def downSight(tBoard, tWBoard):
    #메두사 위치 찾고, 아래시야 설정
    meduR, meduC = -1,-1
    for r in range(N):
        for c in range(N):
            if tBoard[r][c]==5:
                meduR,meduC=r,c
    # print("메두사위치:", meduR, meduC )
    leftC = meduC
    rightC = meduC
    sightBoard = [[0]*N for _ in range(N)] # 1은 메두사가 보고있는구역
    
    #1. 메두사 밑 구역 설정/전사 수 싹 세기
    allWarriorsInSight = 0
    for r in range(meduR+1,N):
        leftC-=1
        rightC+=1
        for c in range(leftC,rightC+1):
            if isInBoard(r,c):
                sightBoard[r][c] = 1
                if len(tWBoard[r][c])>0:
                    allWarriorsInSight+=len(tWBoard[r][c])

    #시야 안에 있는 전사별로 그 이하 메두사가 못보는 구역 설정
    #이때 사라진 전사들은 메두사가 본것에서 숫자 제외
    for i in range(N):
        for j in range(N):
            if sightBoard[i][j]==0:
                continue
            if len(tWBoard[i][j])==0:
                continue
            #현위치가 기존의 메두사 시야구역이고,
            #전사가 존재할경우 그 밑으로 사각지대 설정
            wLeftC = j
            wRightC = j
            for r in range(i+1,N):
                if j<meduC: #메두사보다 왼쪽인경우
                    wLeftC-=1
                    for c in range(wLeftC,j+1):
                        if isInBoard(r,c):
                            if sightBoard[r][c]==1:
                                allWarriorsInSight-=len(tWBoard[r][c])
                            sightBoard[r][c]=0
                            
                elif j==meduC:
                    if sightBoard[r][j]==1:
                        allWarriorsInSight-=len(tWBoard[r][j])
                    sightBoard[r][j]=0
                    
                else:
                    wRightC+=1
                    for c in range(j,wRightC+1):
                        if isInBoard(r,c):
                            if sightBoard[r][c]==1:
                                allWarriorsInSight-=len(tWBoard[r][c])
                            sightBoard[r][c]=0
    return allWarriorsInSight, sightBoard

def findMeduMaxDir():
    """
    output : (stonedWarriors, possibleMoveMap)
    현재 자리에서 4방향중 가장 많이 사람 석화하는 방향 찾고,
    그 사람 수와, 음영 지도 리턴
    그냥 지도에 메두사를 기록해두고 지도를 돌려서 찾자!!
    """

    tmpBoard = copy.deepcopy(BoardArr)
    tmpWarriorBoard = copy.deepcopy(WarriorBoard)

    dirCheckList = [] #하,우,상,좌 순으로 배치됨(회전수 0, 1,2,3)
    sightBoardList = []
    
    for i in range(4):
        # print("방향:", i)
        stonedCnt,sBoard = downSight(tmpBoard, tmpWarriorBoard)
        tmpBoard = list(zip(*tmpBoard[::-1]))
        tmpWarriorBoard = list(zip(*tmpWarriorBoard[::-1]))
        dirCheckList.append(stonedCnt)
        sightBoardList.append(sBoard)
    
    #max 찾은 위치에서 stonedCnt, tmpWarriorBoard 리턴
    result = max(dirCheckList)
    idxs = [2,0,3,1]
    resultIdx = 2
    for i in range(4): 
        idx = idxs[i]
        if result ==dirCheckList[idx]:
            resultIdx = idx
            break
    
    # 이제 음영구역 만들어서 리턴
    shadowBoard = sightBoardList[resultIdx]

    # 회전수에 맞게 원래 방향으로 만들어서 리턴
    for _ in range((4-resultIdx)%4):
        shadowBoard = list(zip(*shadowBoard[::-1]))

    return result, shadowBoard

def calDist(r1,c1, r2,c2):
    return abs(r1-r2)+abs(c1-c2)

def warriorMovePhase(MoveMap, meduR, meduC):
    global WarriorBoard
    #돌로 변하지 않은 전사들은
    # 메두사를 향해 두칸까지 이동

    # 번호별 관리
    WarriorCoordsDict = {}
    for r in range(N):
        for c in range(N):
            for i in range(len(WarriorBoard[r][c])):
                WarriorNum = WarriorBoard[r][c][i]
                WarriorCoordsDict[WarriorNum] = [r,c]
    moveCnt = 0
    for WarriorNum in WarriorCoordsDict:
        r,c = WarriorCoordsDict[WarriorNum]
        if MoveMap[r][c]==1:
            continue
        oriDist = calDist(r,c,meduR,meduC)
        moveList = []
        for dr,dc in [(-1,0),(1,0),(0,-1),(0,1)]:
            nr,nc = r+dr, c+dc
            if isInBoard(nr,nc) and MoveMap[nr][nc]==0 and oriDist>calDist(nr,nc,meduR,meduC):
                moveList.append((nr,nc))
        if len(moveList)==0:
            continue
        moveCnt+=1
        tR,tC = moveList[0]
        oriDist = calDist(tR,tC,meduR,meduC)
        moveList = []
        for dr,dc in [(0,-1),(0,1),(-1,0),(1,0)]:
            nr,nc = tR+dr, tC+dc
            if isInBoard(nr,nc) and MoveMap[nr][nc]==0 and oriDist>calDist(nr,nc,meduR,meduC):
                moveList.append((nr,nc))
        if len(moveList)!=0:
            tR,tC = moveList[0]
            moveCnt+=1
        WarriorCoordsDict[WarriorNum] = [tR,tC]

    #다시 지도화하기
    WarriorBoard = [[[] for _ in range(N)]for _ in range(N)]
    for WarriorNum in WarriorCoordsDict:
        r,c = WarriorCoordsDict[WarriorNum]
        WarriorBoard[r][c].append(WarriorNum)

    return moveCnt
    
def WarriorAttackPhase(meduR,meduC):
    if len(WarriorBoard[meduR][meduC])>0:
        result = len(WarriorBoard[meduR][meduC])
        WarriorBoard[meduR][meduC] = []
        return result
    return 0


#!!!!!----작동시작-----!!!!

#입력부 및 변수
N, M = map(int,input().split())
sR, sC, eR, eC = map(int,input().split())
tmp = list(map(int,input().split()))

WarriorBoard = [[[] for _ in range(N)]for _ in range(N)]
WarriorCoords = []
wId = 0
for i in range(0,M*2,2):
    WarriorCoords.append([tmp[i],tmp[i+1]])
    WarriorBoard[tmp[i]][tmp[i+1]].append(wId)
    wId+=1
BoardArr = [list(map(int,input().split())) for _ in range(N)]

#메두사 경로 미리뽑기
meduRoute = bfs(sR,sC, eR,eC)
meduRoute.reverse()
# print(meduRoute)
if len(meduRoute)==0:
    print(-1)
#메두사 이동시작
for i in range(1,len(meduRoute)):
    mR,mC = meduRoute[i]
    if (mR,mC)==(eR,eC):
        print(0)
        break
    
    #메두사이동
    BoardArr[mR][mC]=5
    #이미 전사가 있다면 전사 사라짐
    if len(WarriorBoard[mR][mC])>0:
        WarriorBoard[mR][mC].clear()

    #4방향중 가장많은 전사 잡을 수 있는 방향 탐색, 결정
    #돌된 사람수와, 전사들이 이동할수 있는 지도 받아오기
    stonedWarriors, possibleMoveMap = findMeduMaxDir()

    #전사 이동
    warriorMoveSum = warriorMovePhase(possibleMoveMap, mR,mC)

    #전사공격
    warriorAttackCnt = WarriorAttackPhase(mR,mC)

    print(warriorMoveSum,stonedWarriors, warriorAttackCnt)
    BoardArr[mR][mC] = 0