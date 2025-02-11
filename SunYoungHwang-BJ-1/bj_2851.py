# 슈퍼마리오

mush = [int(input()) for _ in range(10)]
sum_mush = 0
for i in range(10):
    sum_mush += mush[i]
    if sum_mush == 100:
        print(sum_mush)
        break
    elif sum_mush-mush[i]<100 and sum_mush > 100:
        if abs(sum_mush-100) <= abs(100-(sum_mush-mush[i])):
            print(sum_mush)
            break
        else:
            print(sum_mush-mush[i])
            break
