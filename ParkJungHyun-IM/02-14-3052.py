nums = [0]*10
for i in range(10):
    nums[i] = int(input())
nums = [i%42 for i in nums]
# print(nums)

# 1. set 이용
# nums = set(nums)
# print(len(nums))

# 2. not in 활용
remain = [nums[0]]
for num in nums:
    if num not in remain:
        remain.append(num)
print(len(remain))

# len 함수 사용하지 않는 법
# cnt=0
# for _ in remain:
#     cnt+=1
# print(cnt)

"""
백준 링크:
https://www.acmicpc.net/problem/3052
"""