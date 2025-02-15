def num_rect(n):
    cnt = 0
    for i in range(1, n+1):
        for k in range(i, n+1):
            if i * k > n:
                break
            cnt+=1
    return cnt


n = int(input())
print(num_rect(n))

"""
백준 링크:
https://www.acmicpc.net/problem/8320

- 접근법

- ! : 앞에서 센 경우
- !! : 주어진 숫자보다 큰 경우
주어진 숫자: 6
1*1 , 1*2 , 1*3 , ... , 1*6
2*1!, 2*2 , 2*3 , 2*4!! : break
3*1!, 3*2!, 3*3!! : break

=> i, j 둘다 for문으로 구성
=> 앞에서 센 경우를 없애주기 위해 j의 시작지점 i로
=> 주어진 숫자보다 큰 경우 break를 활용해 for문 탈출

"""