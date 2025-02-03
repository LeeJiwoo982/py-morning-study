# 가위1, 바위2, 보3
# a와b 중 이긴사람 판별. 비김X
# a이기면 A, 
# 1 <2, 2<3, 3<1
A, B = 3, 2
# b이김
    # 3(가바), 5(바보), 4(보가)
s = A + B
if s == 3:
    if A == 1:
        print("B")
    else:
        print('A')
elif s ==5:
    if A ==2:
        print("B")
    else:
        print('A')

elif s == 4:
    if A ==3:
        print('B')
    else:
        print('A')