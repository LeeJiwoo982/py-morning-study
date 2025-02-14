def deliver(N):
    count = 0
    n=N
    while n>=0:
        if n%5==0:
            return count+n//5
        n-=3
        count+=1
    return -1

    # min_del = N
    # if (N%3)%5 == 0:
    #     num_del = N//3 + N%3//5
    #     if num_del < min_del:
    #         min_del = num_del
    # if (N%5)%3 == 0:
    #     num_del = N//5 + N%5//3
    #     if num_del < min_del:
    #         min_del = num_del
    # if min_del == N:
    #     return -1
    # else:
    #     return min_del


N = int(input())
print(deliver(N))

"""
백준 링크:
https://www.acmicpc.net/problem/2839
블로그 링크:
https://ooyoung.tistory.com/81
"""