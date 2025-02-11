tar_str = list(input())
cnt = 0
ch_al = ['c=', 'c-', 'd-', 'lj', 'nj', 's=', 'z=']
new_str = list(tar_str)

# 새로운 행렬 사용 
for j in range(len(tar_str)-2):
    if ''.join(tar_str[j:j+3]) == 'dz=':
        cnt += 1
        tar_str[j:j+3] = ['0']

for i in range(len(tar_str)-1):
    if ''.join(tar_str[i:i+2]) in ch_al:
        cnt += 1
        tar_str[i:i+2] =['0']

cnt += sum([1 for i in tar_str if i != '0'])
print(tar_str)
print(cnt)


## 합 활용
# for j in range(len(tar_str)-2):
#     if ''.join(tar_str[j:j+3]) == 'dz=':
#         tar_str[j:j+3] =[str(1/3)]

# for i in range(len(tar_str)-1):
#     if ''.join(tar_str[i:i+2]) in ch_al:
#         tar_str[i:i+2] = [str(1/2)]
    
# for k in range(len(tar_str)):
#     if not tar_str[k].isdecimal():
#         tar_str[k] = '1'

# print(sum(map(int, tar_str)))

## GPT 선생님
# tar_str = input().strip()
# ch_al = ['dz=', 'c=', 'c-', 'd-', 'lj', 'nj', 's=', 'z=']

# cnt = 0
# for ch in ch_al:
#     cnt += tar_str.count(ch)  # 크로아티아 알파벳 개수 세기
#     tar_str = tar_str.replace(ch, ' ')  # 카운트한 부분 제거

# # 남은 문자 개수 추가
# cnt += len(tar_str.replace(' ', ''))  
# print(cnt)

## GPT 선생님 ver 2
# tar_str = input().strip()
# ch_al = ['dz=', 'c=', 'c-', 'd-', 'lj', 'nj', 's=', 'z=']

# for ch in ch_al:
#     tar_str = tar_str.replace(ch, '0')  # 크로아티아 알파벳을 '0'으로 변경

# print(len(tar_str))  # 변경 후 길이 출력