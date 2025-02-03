T = int(input())
 
numbers = []
for i in range(T):
  values = list(map(int, input().split()))
  numbers.append(values)
 
for i in range(T):
  n, m = numbers[i]  
  if n > m:
    print(f"#{i+1} >")
  elif n == m:
    print(f"#{i+1} =")
  else:
    print(f"#{i+1} <")