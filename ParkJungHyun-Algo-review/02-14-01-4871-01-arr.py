# 인접 행렬, dfs로 4871번 풀기
def dfs(S, G):
    global visited, arr, result, V
    if result==1:
        return
    for i in range(1, V+1):
        if arr[S][i]==1 and visited[i]==False:
            if i==G:
                result = 1
            visited[i]=True
            dfs(i, G)



T = int(input())
for tc in range(1, T+1):
    V, E = list(map(int, input().split()))
    arr = [[0]* (V+1) for _ in range(V+1)] # VxV 배열 만들기, 인덱스 똑같게
    for i in range(E):
        a, b = list(map(int, input().split()))
        arr[a][b] = 1 # a -> b의 경로 가능하다
    S, G = list(map(int, input().split()))
    # print(arr, V, E, S, G)
    visited = [False] * (V+1)
    result = 0
    dfs(S, G)
    print(f"#{tc} {result}")
