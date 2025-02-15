def sudoku_verify(arr):
    N=9
    """
    1. 함수를 만들어서 체크한다
    2. 함수안에 arr가 들어오면
    3. 각 행별로 cor verify
    4. 각 열별로 line verify
    5. 각 사각 별로 square verify
    """
    cor = [0]*(N+1)
    line = [0]*(N+1)
    square = [0]*(N+1)
    # 행 별로 cor verify
    for i in range(N):
        for j in range(N):
            if cor[arr[i][j]]:
                return 0
            cor[arr[i][j]]+=1
        print(cor)
        cor = [0]*(N+1)
    # 열 별로 line verify
    for j in range(N):
        for i in range(N):
            if line[arr[i][j]]:
                return 0
            line[arr[i][j]]+=1
        print(line)
        line = [0]*(N+1)
    # 사각 별로 square verify
    M=3
    for i in range(N):
        for j in range(N):
            if i%3==0 and j%3==0:
                for n in range(M):
                    for m in range(M):
                        if [square[arr[i+n][j+m]]]:
                            return 0
                        square[arr[i+n][j+m]]+=1
                square=[0]*(N+1)
    return 1