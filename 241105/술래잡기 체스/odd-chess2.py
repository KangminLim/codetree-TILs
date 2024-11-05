di, dj = [-1,-1,0,1,1,1,0,-1], [0,-1,-1,-1,0,1,1,1]
v = [[[0] * 2 for _ in range(4)] for _ in range(4)]
for i in range(4):
    fish_lst = list(map(int,input().split()))
    for j in range(4):
        v[i][j] = [fish_lst[j*2],fish_lst[j*2+1]-1]

def find(idx,v):
    for i in range(4):
        for j in range(4):
            if v[i][j][0] == idx: # 찾던 물고기 번호면
                return i,j,v[i][j][1]

def dfs(si,sj,sd,sm,v):
    global ans
    ans = max(ans,sm)

    for idx in range(1,17):
        ci,cj,dr = find(idx,v)
        if dr == -1: continue # 물고기 없음
        for j in range(8):
            td = (dr+j)%8
            ni,nj = ci+di[td], cj+dj[td]
            if 0<=ni<4 and 0<=nj<4 and (ni,nj) != (si,sj):
                v[ci][cj][1] = td
                v[ci][cj],v[ni][nj] = v[ni][nj], v[ci][cj]
                break

    for mul in range(1,4):
        ni,nj = si+di[sd] * mul, sj+dj[sd]*mul
        if 0<=ni<4 and 0<=nj<4 and v[ni][nj][1] != -1:
            fn,fd = v[ni][nj]
            v[ni][nj][1] = -1 # 물고기 먹음 처리
            nv = [[x[:] for x in lst] for lst in v]

            dfs(ni,nj,fd,sm+fn,nv)

            v[ni][nj][1] = fd # 원상복구

ans = 0
fn, fd = v[0][0]
v[0][0][1] = -1
dfs(0,0,fd,fn,v)
print(ans)