# 스탬프 찍기
# 주어진 숫자만큼 # 출력하기

a=int(input())
for i in range(1, a+1):
    print('#', end='')
    # print 끝에 개행을 하지 않으려면 end=''를 추가