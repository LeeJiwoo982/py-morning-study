nums = list(map(int, input().split()))
# input(): 주어진 입력 문자열 "8 3" 입력받기
# input().split(): 문자열 공백 단위로 쪼갬 ["8","3"]
# map, int: 각각의 문자열을 숫자로 바꿈
# list로 모으기: [8, 3]
 
a, b = nums # 리스트이 각 원소를 꺼내서 a, b에 저장
print(a+b)
print(a-b)
print(a*b)
print(a//b)