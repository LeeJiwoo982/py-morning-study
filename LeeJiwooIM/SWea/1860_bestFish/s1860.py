import sys
sys.stdin = open('input.txt', 'r')

# N명의 사람만 먹을 수 있는 붕어빵
# 0초부터 만들기 시작 M초의 시간에 K개의 붕어빵을 만듬
# 완성과 함께 다음 붕어빵 만들기 가능
T = int(input())
for tc in range(1, T+1): # 1
    N, M, K = map(int, input().split()) [2,2,2]
    # 손님 정보 배열 밭기
    customers = list(map(int, input().split())) #[3, 4]
