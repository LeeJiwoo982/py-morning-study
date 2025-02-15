T = int(input())
numbers = []
for i in range(T):
  values = list(map(int, input().split()))
  numbers.append(values)
 
for i in range(T):
  big = max(numbers[i])
  small = min(numbers[i])
  print(f"#{i+1} {big//small} {big%small}")