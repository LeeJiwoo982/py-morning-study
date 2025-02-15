def switch(N, arr, A, B):
    if A == 1:  # 남학생일때
        for i in range(N):
            if (i + 1) % B == 0:
                arr[i] = ~arr[i] + 2
                # val = arr[i]
                # if val == 1: arr[i] = 0
                # else: arr[i] = 1

                # 강사님 방법:
                # arr[i] = (arr[i]+1)%2

    if A == 2:  # 여학생일때
        i = B - 1  # 인덱스
        arr[i] = ~arr[i] + 2
        n = 0
        while i - n >= 0 and i + n < N:
            if arr[i - n] == arr[i + n]:
                arr[i - n] = ~arr[i - n] + 2
                arr[i + n] = ~arr[i + n] + 2
                n += 1
            else:
                break
    return arr


N = int(input())
arr = list(map(int, input().split()))
stu = int(input())
for _ in range(stu):
    A, B = list(map(int, input().split()))
    arr = switch(N, arr, A, B)

for i in range(N // 20):
    for j in range(20):
        print(arr[i * 20 + j], end=' ')
    print('')
for i in range(N % 20):
    print(arr[(N // 20) * 20 + i], end=' ')

# 20개씩 끊어서 출력
# for i in range(1, N+1, 20):
#     print(' '.join([str(n) for n in arr[i:i+20]]))