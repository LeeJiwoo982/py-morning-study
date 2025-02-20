def min_sum(r, sum):
    global visited, cnt, min_num, arr, N
    cnt+=1

    if sum > min_num:
        return
    if visited == [True] * N:
        if sum < min_num:
            min_num = sum
            return
    if r>=N:
        return

    for c in range(N):
        if not visited[c]:
            visited[c] = True
            min_sum(r+1, sum+arr[r][c])
            visited[c] = False


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    min_num = 100000000
    cnt = 0
    visited = [False]*N
    min_sum(0, 0)
    print(f"#{tc} {min_num}, {cnt}")
    # print(f"#{tc} {min_num}")


"""
3번 제한시간 초과 났음.
-----------------------------------------------------
1번 시도 - 제한시간 초과 (5 fail)

def min_sum(i, j):
    global min_num, sum_num, N, arr, visited_i, visited_j

    if (visited_j == [True]*N) and (visited_i == [True]*N):
        if sum_num < min_num:
            min_num = sum_num
        return

    for r in range(N):
        for c in range(N):
            if not visited_i[r] and not visited_j[c]:
                visited_i[r] = True
                visited_j[c] = True
                sum_num += arr[r][c]
                min_sum(r, c)
                sum_num -= arr[r][c]
                visited_i[r] = False
                visited_j[c] = False



T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    min_num = 100000000
    sum_num = 0

    visited_i = [False]*N
    visited_j = [False]*N
    min_sum(0, 0)
    print(f"#{tc} {min_num}")
-------------------------------------------------
2번 시도 - 제한시간 초과 (5 fail)

def min_sum(i, j):
    global min_num, sum_num, N, arr, visited_i, visited_j
    # cnt+=1
    if sum_num > min_num:
        return     ##################여기! 합한 값이 min값 보다 클 경우 바로 반환
    if (visited_j == [True]*N) and (visited_i == [True]*N):
        if sum_num < min_num:
            min_num = sum_num
        return

    for r in range(N):
        for c in range(N):
            if not visited_i[r] and not visited_j[c]:
                visited_i[r] = True
                visited_j[c] = True
                sum_num += arr[r][c]
                min_sum(r, c)
                sum_num -= arr[r][c]
                visited_i[r] = False
                visited_j[c] = False



T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    min_num = 100000000
    sum_num = 0
    # cnt = 0
    visited_i = [False]*N
    visited_j = [False]*N
    min_sum(0, 0)
    print(f"#{tc} {min_num}")
---------------------------------------------------------
3번 시도 - 제한시간 초과 (4 fail)

def min_sum(i, j):
    global min_num, sum_num, N, arr, visited_i, visited_j, cnt
    cnt+=1
    if sum_num > min_num:
        return
    if (visited_j == [True]*N) and (visited_i == [True]*N):
        if sum_num < min_num:
            min_num = sum_num
        return

    for r in range(i,N): ###################### 여기! 모든 i에 대해서 도는 게 아님!
        for c in range(N):
            if not visited_i[r] and not visited_j[c]:
                visited_i[r] = True
                visited_j[c] = True
                sum_num += arr[r][c]
                min_sum(r, c)
                sum_num -= arr[r][c]
                visited_i[r] = False
                visited_j[c] = False



T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    min_num = 100000000
    sum_num = 0
    cnt = 0
    visited_i = [False]*N
    visited_j = [False]*N
    min_sum(0, 0)
    # print(f"#{tc} {min_num}, {cnt}")
    print(f"#{tc} {min_num}")
----------------------------------------------------------
4번 시도 - Pass

def min_sum(i, j):
    global min_num, sum_num, N, arr, visited_i, visited_j, cnt
    cnt+=1
    # print(i, j)
    if sum_num > min_num:
        return
    if (visited_j == [True]*N) and (visited_i == [True]*N):
        if sum_num < min_num:
            min_num = sum_num
        return

    for r in range(i,N):
        for c in range(N):
            if not visited_i[r] and not visited_j[c]:
                visited_i[r] = True
                visited_j[c] = True
                sum_num += arr[r][c]
                min_sum(r, c)
                sum_num -= arr[r][c]
                visited_i[r] = False
                visited_j[c] = False
        if visited_i[r]==False: ##################### 여기! i를 다 돌고나서 i 결과가 False일때 반환
            return



T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    min_num = 100000000
    sum_num = 0
    cnt = 0
    visited_i = [False]*N
    visited_j = [False]*N
    min_sum(0, 0)
    # print(f"#{tc} {min_num}, {cnt}")
    print(f"#{tc} {min_num}")
--------------------------------------------------------------
5번째 시도 - 강사님의 도움, 훨씬 더 간단한 코드, 생각하기 편하다.
cnt 개수가 줄진 않았음. 호출하면 그때 판단하기 때문인듯

def min_sum(r, sum):
    global visited, cnt, min_num, arr, N
    cnt+=1

    if sum > min_num:
        return
    if visited == [True] * N:
        if sum < min_num:
            min_num = sum
            return


    for c in range(N):
        if not visited[c]:
            visited[c] = True
            min_sum(r+1, sum+arr[r][c])
            visited[c] = False


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    min_num = 100000000
    cnt = 0
    visited = [False]*N
    min_sum(0, 0)
    print(f"#{tc} {min_num}, {cnt}")
    # print(f"#{tc} {min_num}")

"""