# 홀수만 더하기
T = int(input())
for i in range(1, T+1):
    numbers=list(map(int, input().split()))
    sum_of_num=0
    for num in numbers:
        if num%2 == 1:
            sum_of_num+=num
    print(f"#{i} {sum_of_num}")