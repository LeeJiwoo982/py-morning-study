# 평균값 구하기
T = int(input())
for i in range(1, T+1):
    numbers=list(map(int, input().split()))
    print(f"#{i} {round(sum(numbers)/len(numbers))}")