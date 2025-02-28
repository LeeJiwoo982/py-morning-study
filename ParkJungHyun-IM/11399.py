def wait_time(N, P):
    # P.sort() # 정렬
    max_p = max(P)
    cnt_arr = [0]*(max_p+1)
    for i in range(N):
        cnt_arr[P[i]]+=1
    for i in range(1, max_p+1):
        cnt_arr[i] += cnt_arr[i-1]
    new_arr=[0]*N
    for i in range(N):
        new_arr[cnt_arr[P[i]]-1]=P[i]
        cnt_arr[P[i]]-=1
    sum_p=0
    for i in range(N):
        # 누적합(처음부터 i까지)의 합
        sum1 = 0
        for j in range(i+1):
            sum1+=new_arr[j]
        sum_p+=sum1
    return sum_p


N = int(input())
P = list(map(int, input().split()))
print(wait_time(N, P))

"""
간단한 구상

def wait_time(N, P):
    P.sort() # 정렬
    sum_p=0
    for i in range(N):
        # 누적합(처음부터 i까지)의 합
        sum_p += sum(P[0:i+1])
    return sum_p
    
백준 링크:
https://www.acmicpc.net/problem/11399
"""