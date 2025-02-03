# 중간값 찾기
N = int(input())
scores=list(map(int, input().split()))
scores=sorted(scores)
print(scores[N//2])