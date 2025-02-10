import sys
sys.stdin = open('simple.txt', 'r')

# N명의 사람만 먹을 수 있는 붕어빵
# 0초부터 만들기 시작 M초의 시간에 K개의 붕어빵을 만듬
# 완성과 함께 다음 붕어빵 만들기 가능

T = int(input())
for tc in range(1, T+1):
    N, M, K = map(int, input().split())
    # 손님 도착 시간
    C = list(map(int, input().split()))
    C.sort()
    bread = 0
    time = 0

    for c in C:
        while time + M <= c:
            time += M
            bread += K

        if bread <= 0:
            print(f'#{tc} Impossible')
            break
        bread -=1
    else:
        print(f'#{tc} Possible')