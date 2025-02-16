# 전체 도화지 크기 100*100
# 색종이 크기 10*10
# 배열로 해서 색종이 있으면 +1하고
# 겹치게 되면 그 수만큼 제외하기
# 인덱스가 P[x+i][y+i]
P = [[0]*100 for _ in range(100)]   #도화지 배열
N = int(input())#색종이 수= 최대 넓이 10*10*N여기서 빼기로 가기

for _ in range(N):
    x, y = map(int, input().split())
    # 색종이 하나씩 P배열에 차지하는 자리에 +1
    for i in range(10):
        for j in range(10):
            P[x+i][y+j] += 1

# 겹치는 부분을 제외한 값
cnt = 0
for row in P:
    for c in row:
        if c > 0: #색종이가 붙어 있다면
            cnt +=1
print(cnt)