# 삼성시의 버스 노선

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    line = [list(map(int, input().split())) for _ in range(N)]
    P = int(input())
    stop = [int(input()) for _ in range(P)]
    ans = [0]*P
    for i in range(N):
        for j in range(P):
            if line[i][0]<= j+1 <= line[i][1]:
                ans[j] += 1

    print(f'#{tc} {" ".join(map(str, ans))}')