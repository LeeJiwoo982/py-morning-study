# 비번 P는 000 ~ 999 중 하나
# 주어진 번호 K부터 1씩 증가하여 비번 확인

#p 123, k 100 
P, K = map(int, input().split())  #정수두개 입력
trial = 1 #시도횟수 변수
while P != K : # P=K가 같아질 때 멈춤
    if P > K:
        K += 1

    else:
        K -= 1
    trial += 1

print(trial)

