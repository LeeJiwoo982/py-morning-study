# 몫과 나머지 출력하기
T = int(input())
for test_case in range(1, T + 1):
    a, b = map(int, input().split())
    print('#%d' %test_case, a//b, a%b)

    # 파이썬의 경우 a/b를 하면 int여도 소수점을 포함해서 결과를 출력
    # 몫을 출력하고 싶을 경우 a//b를 넣어야
    # #1 과 같이 문자와 숫자를 붙여쓰거나 하고 싶은 경우 '변수 포멧' 이용
    # 변수 포멧: %d: 정수(int), %f: 실수(float), %s: 문자열(spring), %c: 문자(character)