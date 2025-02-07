import sys
sys.stdin =open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    arr = list(map(int, input().split()))

    max_v = 0
    for num in arr:
        if max_v < num:
            max_v = num
    print(f'#{tc} {max_v}')
