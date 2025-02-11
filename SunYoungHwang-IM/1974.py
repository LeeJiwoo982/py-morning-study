# 스도쿠 검증

T = int(input())

def sudoku(row):
    # 행 확인
    for r in row:
      if sum(r) != 45:
        return 0
    # 열 확인
    for c in zip(*row):
      if sum(c) != 45:
        return 0
    # 칸 확인
    for i in range(0,9,3):
      for j in range(0,9,3):
        sum_arr = 0
        for k in range(3):
          for l in range(3):
            sum_arr += row[i+k][j+l]
        if sum_arr !=45:
          return 0
    return 1


for tc in range(1,T+1):
  arr = []
  for _ in range(9):
    arr.append(list(map(int,input().split())))
  print(f'#{tc} {sudoku(arr)}')


# GPT 선생님

def sudoku(arr):
    # 행 확인
    for r in arr:
        if set(r) != {1,2,3,4,5,6,7,8,9}:
            return 0

    # 열 확인
    for c in zip(*arr):
        if set(c) != {1,2,3,4,5,6,7,8,9}:
            return 0

    # 3x3 칸 확인
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            subgrid = set()
            for k in range(3):
                for l in range(3):
                    subgrid.add(arr[i+k][j+l])
            if subgrid != {1,2,3,4,5,6,7,8,9}:
                return 0

    return 1


T = int(input())

for tc in range(1, T + 1):
    arr = [list(map(int, input().split())) for _ in range(9)]
    print(f'#{tc} {sudoku(arr)}')