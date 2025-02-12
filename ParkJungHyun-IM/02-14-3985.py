def expect_max(L, N, P, K):
    point = list(zip(P, K))
    max_idx = 0
    max_val = 0
    for i in range(1, N+1):
        val = point[i][1]-point[i][0]
        if val > max_val:
            max_idx=i
            max_val=val
    return max_idx

def real_max(L, N, P, K):
    point = list(zip(P, K))
    lst = [1]*(L+1)
    max_idx=0
    max_val=0
    for i in range(1, N+1):
        val_sum=0
        for n in range(point[i][0], point[i][1]+1):
            if lst[n]==1:
                val_sum+=1
                lst[n]=0
        if val_sum > max_val:
            max_idx = i
            max_val = val_sum
    return max_idx

L = int(input())
N = int(input())
P = [0]
K = [0]
for i in range(N):
    p, k = list(map(int, input().split()))
    P.append(p)
    K.append(k)
print(expect_max(L, N, P, K))
print(real_max(L, N, P, K))

"""
백준 링크:
https://www.acmicpc.net/problem/3985
참고 블로그 링크:
https://velog.io/@sh93/%EB%B0%B1%EC%A4%80-3985%EB%B2%88-%EB%A1%A4-%EC%BC%80%EC%9D%B4%ED%81%AC-.-python
겹치는 코드가 많아 굳이 두 함수를 따로 만들지 않아도 됐을 것 같다.
"""