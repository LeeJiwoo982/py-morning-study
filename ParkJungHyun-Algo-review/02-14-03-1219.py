def dfs(N):
    global result, visited, arr1, arr2

    if result==1:
        return
    if visited[N]==False and (arr1[N]!=-1 or arr2[N]!=-1):
        visited[N] = True
        if arr1[N]==99 or arr2[N]==99:
            result=1
            return
        if arr2[N]!=-1:
            dfs(arr2[N])
            dfs(arr1[N])
        else:
            dfs(arr1[N])
    pass


for tc in range(1, 11):
    tc, N = list(map(int, input().split()))
    nums = list(map(int, input().split()))
    N = len(nums)
    # 문제에서 주어진대로
    arr1 = [-1]*100
    arr2 = [-1]*100
    for i in range(0, N, 2):
        if arr1[nums[i]] == -1:
            arr1[nums[i]] = nums[i+1]
        else:
            arr2[nums[i]] = nums[i+1]
    visited = [False]*100
    result = 0
    dfs(0)
    print(f"#{tc} {result}")