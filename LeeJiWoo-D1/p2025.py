# 1부터 주어진 숫자만큼 더한 값 출력

number = int(input())
n = 0
for num in range(1, number+1):
    n += num

print(n)