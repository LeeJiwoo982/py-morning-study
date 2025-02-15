T = int(input())
 
numbers = []
for i in range(T):
    values = list(map(int, input().split()))
    numbers.append(values)
 
for n in range(T):
    a=0
    for m in numbers[n]:
        if m%2==1:
            a+=m
    print(f"#{n+1} {a}")