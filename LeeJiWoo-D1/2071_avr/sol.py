import sys
sys.stdin =open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    arr = list(map(int,input().split()))
    total = 0
    for num in arr:
        total += num

    total_avr = round(total / len(arr))
    print(f'#{tc} {total_avr}')
