# 직사각형을 만드는 방법
n =  int(input())
# 주어진 수로 만들어질 수 있는 정사각형의 개수가 중요.
# 정사각형의 크기는 k*k
k = 0
while k*k <= n:
    k += 1
    for i in range(1, k+1):
        if (i-1)*(i-1) < n <= i * i:
            pass