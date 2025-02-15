import sys
sys.stdin =open('s_input.txt', 'r')
# CountingSort의 단계 활용

T = int(input())    # TestCase Number

for tc in range(1, T+1):
    N = int(input())    # N=2 버스대수
    # 버스1은 정류장 번호가 1번 이상이고 3번 이하인 모든 정류장을 다니는 버스노선
    # 버스2는 정류장 번호가 2번 이상이고 5번 이하인 모든 정류장을 다니는 버스노선
    arr = [list(map(int, input().split())) for _ in range(N)]
    P = int(input()) # 버스정류장 개수
    # P개의 버스정류장을 의미하는 배열
    # C = [int, input() for _ in range(P)]
    C = [0] * P
    for j in range(P):
        C[j] = int(input())
    # print(C)
    k = max(C)
    cnt = [0] * (k+1)
    # 정차 버스정류장 체크
    for i in range(N):
        A, B = arr[i]
        # print(type(A), type(B)) 인트형
        for j in range(P):
            cnt[C[j]] += 1
    # print(cnt)

    C = list(map(str, C))
    C = ' '.join(C)
    print(f'#{tc} {cnt} {C}')
