# 직사각형을 만드는 방법
n =  int(input())
# 주어진 수로 만들어질 수 있는 정사각형의 개수가 중요.
# 정사각형의 크기는 k*k
k = 1

cnt = n
while n>=k**2:
    k += 1
    for i in range(2, k+1):
        if (i-1)**2 < n <= i ** 2:
            cnt += n//i -(i-1)

print(cnt)