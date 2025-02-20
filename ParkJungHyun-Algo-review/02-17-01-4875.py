def find_start(N, arr):
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 2:
                return [i, j]


def maze(i, j):
    global N, arr, result, visited
    if result == 1:
        return
    visited[i][j]=1
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]
    for n in range(4):
        ni = i + di[n]
        nj = j + dj[n]
        if 0<=ni<N and 0<=nj<N:
            if arr[ni][nj]==3:
                result=1
                return
            if arr[ni][nj] == 0 and visited[ni][nj]==0:
                maze(ni, nj)



T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]
    i, j = find_start(N, arr)
    visited = [[0]*N for _ in range(N)]
    for r in range(N):
        for c in range(N):
            if arr[r][c]!=0:
                visited[r][c]=1
    result = 0
    maze(i, j)
    print(f"#{tc} {result}")