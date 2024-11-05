arr1 = [[0] * 4 for _ in range(6)]
arr2 = [[0] * 4 for _ in range(6)]
tbl = {1:1, 2:3, 3:2}

def domino(arr,type,j):
    global ans
    # [1] 블럭 떨구기 (위에서 아래로.. 마지막 성공위치 : 실패시 직전 행)
    if type == 1: # 한개짜리
        for i in range(2,6):
            if arr[i][j] != 0: # 블럭 놓을 수 없음 => 직전행에 놓기
                arr[i-1][j] = 1
                break
        else:   # 모두가능(마지막 위치 -> 바닥 칸)
            arr[5][j] = 1
    elif type == 2: # 가로 * 2 (j,j+1)
        for i in range(2,6):
            if arr[i][j] != 0 or arr[i][j+1]:
                arr[i-1][j] = arr[i-1][j+1]=1
                break
        else:
            arr[5][j] = arr[5][j+1] = 1
    else: # 세로 * 2 체크는 한칸만, 배치는 두개 (i,i+1)
        for i in range(2,6):
            if arr[i][j] != 0:
                arr[i-1][j] = arr[i-2][j]=1
                break
        else:
            arr[5][j] = arr[4][j] = 1

    # [2] 4개가 완성된 경우 ans+1, 해당줄 삭제(0번에 모두 0인 행 추가)
    for i in range(2,6):
        if sum(arr[i]) == 4: # 행이 모두 블럭인 경우
            ans += 1
            arr.pop(i)
            arr.insert(0,[0]*4)

    # [3] 0,1 행에 블럭 있으면 그 행 수만큼 제일 아래에서 삭제
    while sum(arr[1]) > 0: # 연한 색에 블럭 있는 경우
        arr.pop(5) # 가장 아래 행 삭제
        arr.insert(0, [0] * 4) # 제일 위 추가

    return arr

ans = 0
N = int(input())
for _ in range(N):
    type,i,j = map(int,input().split())

    arr1 = domino(arr1,type,j) # 행단위 처리
    arr2 = domino(arr2,tbl[type],i) # 열단위 처리

cnt = sum(map(sum,arr1)) + sum(map(sum,arr2))
print(ans,cnt,sep='\n')