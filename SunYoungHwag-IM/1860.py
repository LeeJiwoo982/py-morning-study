# 진기의 최고급 붕어빵

## GPT 선생님 
T = int(input())  # 테스트 케이스 개수

for tc in range(1, T+1):
    N, M, K = map(int, input().split())  # 손님 수 N, M초마다 K개 생산
    customers = list(map(int, input().split()))  # 손님 도착 시간

    customers.sort()  # 손님 도착 시간 오름차순 정렬
    possible = True  # 붕어빵 제공 가능 여부
    for i in range(N):
        time = customers[i]
        available_bread = (time // M) * K  # 해당 시간까지 만들어진 붕어빵 수
        if available_bread < (i + 1):  # 도착한 손님 수보다 붕어빵이 적다면
            possible = False
            break  # 더 이상 확인할 필요 없음

    result = "Possible" if possible else "Impossible"
    print(f"#{tc} {result}")