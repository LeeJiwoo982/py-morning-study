# 알파벳을 숫자로 변환
# print(ord('a')) # ord: 아스키코드로 변환
# 알파벳은 대문자만 들어온다고 가정
# => 알파벳 아스키코드 숫자에서 64를 빼면 A=1
alphabet = input()
for character in alphabet:
    print(ord(character)-64, end=' ')