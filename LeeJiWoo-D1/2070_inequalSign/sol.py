import sys
sys.stdin =open('input.txt', 'r')

# 두 개의 수 입력받아 크기 비교하여 등호 부등호 출력

T = int(input())
for tc in range(1,T+1):
    a, b = map(int, input().split())
    result = ''
    if a>b: result = '>'
    elif a < b: result = '<'
    else: result = '='

    print(f'#{tc} {result}')