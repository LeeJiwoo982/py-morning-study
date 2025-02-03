number = int(input())
 
# def add_all(num):
#   if num == 0:
#     return 0
#   else:
#     return num+ add_all(num-1)
 
all_sum = 0
for i in range(number+1):
    all_sum += i
 
print(all_sum)
 
# print(add_all(number))