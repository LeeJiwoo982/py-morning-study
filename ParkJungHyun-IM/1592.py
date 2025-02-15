N, M, L = list(map(int, input().split()))
cnt = [0]*N # 초기값 (사람마다 공 받은 횟수)
i=0 # 초기값 (위치)
result=-1 # 초기값 (공 주고받은 횟수, 출력값)
while M not in cnt:
    cnt[i]+=1
    ni = i+L*((cnt[i]%2)*2-1)
    # 공받은 횟수를 짝수와 홀수로 나누기 싫어서
    # cnt[i]%2를 활용해 코드 작성

    # ni가 0보다 작거나 N보다 큰 경우 ni를 처리
    while ni>=N:
        ni-=N
    while ni<0:
        ni+=N
    
    i=ni # 다음 i에 ni 넣어주기
    result+=1 # 공 주고받은 횟수 +1
print(result)

"""
백준링크:
https://www.acmicpc.net/problem/1592
"""