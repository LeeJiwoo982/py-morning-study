# 자연수(1<=n<=9999) 입력 받아 각 자릿수 함을 계산
n = 6789
total = 0
string = str(n)
for s in string:
    total += int(s)

print(total)
