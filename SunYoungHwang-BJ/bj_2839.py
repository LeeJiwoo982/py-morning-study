# 설탕배달

# GPT
N = int(input())

cnt = 0

while N >= 0:
    if N % 5 == 0:  # 5의 배수이면 바로 나눌 수 있음
        cnt += N // 5
        print(cnt)
        break
    N -= 3  # 5의 배수가 아니면 3을 빼고 봉지 하나 추가
    cnt += 1
else:
    print(-1)  # 정확하게 나눌 수 없는 경우

## 진경님 코드

def sugar_delivery(N):

    five_sugar = 0
    three_sugar = 0

    result = -1
    for i in range(N//5+1):
        for j in range(N//3+1):
            if 5*i + 3*j == N:
                five_sugar = i
                three_sugar = j

    if five_sugar + three_sugar > 0:
        result = five_sugar + three_sugar

    return result

n = int(input())
print(sugar_delivery(n))





###남겨두는 이렇게 하면 안됩니다###
# N = int(input())

# total = 0
# cnt = 0
# while total < N:
#   if (N-total) % 5 == 0:
#     cnt += (N-total)//5
#     total = N
#     break
#   elif (N-total) % 3 == 0:
#     cnt += (N-total)//3
#     total = N
#     break
#   else:
#     total += 5
#     cnt += 1


# if total == N:
#   print(cnt)
# else:
#   print(-1)