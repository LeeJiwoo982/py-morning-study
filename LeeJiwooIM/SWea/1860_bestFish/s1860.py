import sys
sys.stdin = open('input.txt', 'r')

# N명의 사람만 먹을 수 있는 붕어빵
# 0초부터 만들기 시작 M초의 시간에 K개의 붕어빵을 만듬
# 완성과 함께 다음 붕어빵 만들기 가능

T = int(input())
for tc in range(1, T+1):
    N, M, K = map(int, input().split())
    # 손님 도착 시간
    C = list(map(int, input().split()))
    C.sort()
    max_v = max(C)
    arr = [0]*(max_v+1)

    # 손님 도착 최대값을 길이로 하는 0 배열에 붕어빵제작 넣기
    for i in range(0, max_v+1, M):
        arr[i] += K

    # 이후에도 영향이 있으라고 누적
    for i in range(1, max_v+1):
        arr[i] += arr[i-1]

    for c in C:
        while arr[c] > 0:
            arr[c] -= 1
            for e in range(c+1, max_v+1):
                arr[e] -= 1

        else