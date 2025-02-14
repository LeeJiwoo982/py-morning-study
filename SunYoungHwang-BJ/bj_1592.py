# 영식이와 친구들

N, M, L = map(int, input().split())
re_ball = [0 for _ in range(N)]

i=0
while max(re_ball)<M:
    re_ball[i] += 1
    if re_ball[i] % 2==0:
        if i+L > N-1:
            i = i+L-N
        else:    
            i += L
