import sys
sys.stdin =open('input.txt', 'r')

# 10개의 수 입력 그 중 홀수만 더하기
T = int(input())
for tc in range(1, T+1):
    arr = list(map(int, input().split()))
    odd_sum = 0

    for odd in arr:
        if odd % 2 == 1:
            odd_sum += odd

    print(f'#{tc} {odd_sum}')