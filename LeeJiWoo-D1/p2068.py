# 10개의 수 입력받아 가장 큰 수 출력
# 0 <= n <=10000

import sys
sys.stdin = open("\Downloads\input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    print(f"#{test_case}", max(list(map(int, input().split(" ")))))