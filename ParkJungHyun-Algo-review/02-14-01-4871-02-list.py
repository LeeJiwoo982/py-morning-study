# 인접 리스트로 4871 풀기
def dfs(S, G):
    global visited, result, V, arr

    if result == 1:
        return
    for i in range(V+1):
        for n in arr[i]:
            if visited[n]==False:
                if n == G:
                    result=1
                    return
                visited[n]=True
                dfs(n, G)
    pass


T = int(input())
for tc in range(1, T+1):
    V, E = list(map(int, input().split()))
    arr = [[] for _ in range(V+1)]
    for _ in range(E):
        A, B = list(map(int, input().split()))
        arr[A].append(B)
    S, G = list(map(int, input().split()))

    visited = [False] * (V+1)
    result = 0
    dfs(S, G)
    print(f"#{tc} {result}")