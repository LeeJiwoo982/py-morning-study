# 1대1 가위바위보
A, B = map(int, input().split())

if ((A==1) and (B==3))or((A==3)and(B==1)):
    if B == 3:
        print('A')
    else:
        print('B')
elif A > B:
    print('A')
else:
   print('B')

# 비기는 경우는 없다
# 가위 1, 바위 2, 보 3
# 1은 3을 이기고 2는 1을 이기고 3은 2를 이김
# 1. 가장 간단한 접근
#    1과 3을 처리하고 나머지는 큰수를 출력
#    if ((A==1) and (B==3))or((A==3)and(B==1)):
#       if B == 3:
#           print('A')
#       else:
#           print('B')
#    elif A > B:
#       print('A')
#    else:
#    print('B')