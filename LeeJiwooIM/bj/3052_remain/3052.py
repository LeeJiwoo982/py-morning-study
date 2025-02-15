#나머지
N = 10
arr = [int(input()) for _ in range(N)]  #10개 의 수 입력받기
# print(arr)
cnt = [0]*42
remain = 0
for i in arr:
    cnt[i%42]+=1
for j in range(42):
    if cnt[j]!=0:
        remain +=1
print(remain)