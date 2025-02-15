# 어디에 단어가 들어갈 수 있을까까
T = int(input())

for tc in range(1,T+1):
    N, K = map(int, input().split())
    arr = []
    for _ in range(N):
        arr.append(list(map(int, input().split())))

    pos = 0
    # 행 확인
    for i in range(N):
        for j in range(N-K+1):
            sum_row = 0
            for k in range(K):
                sum_row += arr[i][j+k]
            if sum_row == K and (j==0 or arr[i][j-1]==0) and (j+K==N or arr[i][j+K]==0):
                pos += 1
    # 열 확인
    for j in range(N):
        for i in range(N-K+1):
            sum_col = 0
            for k in range(K):
                sum_col += arr[i+k][j]
            if sum_col == K and (i == 0 or arr[i - 1][j] == 0) and (i + K == N or arr[i + K][j] == 0):
                pos += 1
    print(f'#{tc} {pos}')


## GPT 선생님

T = int(input())

for tc in range(1, T + 1):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    
    pos = 0

    # 행 확인
    for i in range(N):
        count = 0
        for j in range(N):
            if arr[i][j] == 1:
                count += 1
            else:
                if count == K:
                    pos += 1
                count = 0
        if count == K:  # 마지막 칸에서 확인
            pos += 1

    # 열 확인
    for j in range(N):
        count = 0
        for i in range(N):
            if arr[i][j] == 1:
                count += 1
            else:
                if count == K:
                    pos += 1
                count = 0
        if count == K:  # 마지막 칸에서 확인
            pos += 1

    print(f'#{tc} {pos}')