T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
numbers = []
for i in range(T):
    values = list(map(int, input().split()))
    numbers.append(values)
 
for i in range(T):
    print(f"#{i+1} {max(numbers[i])}")