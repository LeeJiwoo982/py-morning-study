def num_rect(N):
    dp = [0]*301 # N의 최대값: 300
    dp[10] = 1
    dp[20] = 3
    dp[30] = 5
    for i in range(40, N+1, 10):
        dp[i] = dp[i-10] + dp[i-20]*2
        # 이 식에 대한 접근을 생각해 내는게 너무 어렵다!
    return dp[N]


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    print(f"#{tc} {num_rect(N)}")