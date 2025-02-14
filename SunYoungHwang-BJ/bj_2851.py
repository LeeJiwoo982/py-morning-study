# 슈퍼마리오

mush = [int(input()) for _ in range(10)]

def mush_sum(arr):
    sum_mush = 0
    closest = 0
    for mush in arr:
        sum_mush += mush

        if sum_mush == 100:
            return sum_mush
        elif abs(100-sum_mush) <= abs(100-closest):
            closest = sum_mush
    return closest      

print(mush_sum(mush))