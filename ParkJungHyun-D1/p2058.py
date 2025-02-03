# 자릿수 더하기

a=input()
sum=0
for i in range(1,len(a)+1):
    sum+=int(a[i-1])
print(sum)

# 문자열 길이 구하는 법: len(a)
# 문자 > 정수 형변환: int(a[i-1])