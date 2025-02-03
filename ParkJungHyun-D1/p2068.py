# 최대 수 구하기
# 10개 수를 받아, 그 중 가장 큰 수 출력
T = int(input())
for i in range(1, T+1):
    num=list(map(int, input().split()))
    num.sort()
    print(f"#{i} {num[-1]}")