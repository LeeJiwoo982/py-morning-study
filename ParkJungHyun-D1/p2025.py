# N줄 덧셈
a=int(input())
sum=0
for i in range(1, a+1):
    sum+=a
    a-=1
print(sum)