# 두 자연수 a, b는 1-9까지 자연수
# 사칙연산 + - * / 순서로 출력
# 나누기 연산에서 소숫점 이하 수 버린다.``

nums = list(map(int, input().split()))
a, b = nums # 리스트의 각 원소를 꺼내서 a, b에 저장
print(a+b)
print(a-b)
print(a*b)
print(a//b)