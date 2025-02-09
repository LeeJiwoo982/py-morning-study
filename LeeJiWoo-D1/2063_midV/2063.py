import sys
sys.stdin =open('input.txt', 'r')

N = int(input())
arr = list(map(int, input().split()))
k = 0 #arr의 최댓값
for m in range(N):
    if k < arr[m]:
        k = arr[m]
cnt = [0]*(k+1)
temp = [0] * N
#최댓값구하기


#카운트정렬
# 1 : 각 요소 카운트 하기
for i in range(N):
    cnt[arr[i]] += 1

# 2 : 카운트 누적 왼->오
for r in range(1,k+1):
    cnt[r] += cnt[r-1]

# 3: 역순으로 cnt 값 -1 하고 Temp자리에 넣기
for t in range(N-1, -1, -1):
    cnt[arr[t]] -= 1
    temp[cnt[arr[t]]] = cnt[arr[t]]
i = (N-1)//2

# mid_v = temp[99]
# print(mid_v)