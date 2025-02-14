# OX 퀴즈

T = int(input())

for _ in range(T):
  res = input()
  t_s = 0 # 각 O의 점수 계산
  e_s = 0 # 전체 점수 합 계산산
  for r in res:
    if r == 'O':
      e_s += 1
      t_s += e_s
    else:
      e_s = 0

  print(t_s)