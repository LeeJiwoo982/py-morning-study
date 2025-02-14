txt = input()
N = len(txt)
R=1
i=1
while N//i>=i:
    if N%i == 0:
        R = i
    i+=1
C = N//R
# print(R, C)
# R = row, 행
# C = col, 열

arr = [[0]*R for _ in range(C)]
k=0
for i in range(C):
    for j in range(R):
        arr[i][j] = txt[k]
        k+=1
# print(arr)
for j in range(R):
    for i in range(C):
        print(arr[i][j], end='')
# for i in range(2, N//2):
#     if N % i == 0 and N // i < N:
#         C = i
# R = N//C

"""
백준 링크:
https://www.acmicpc.net/problem/2999
참고 블로그 링크:
http://uknowblog.tistory.com/100
(array 안 쓰고 그대로 출력하는 방법
: 구상은 했어도 실험하기가 까다로움, 
시험때 만들기 어려울 것 같음. 
array가 더 까다로울수도 있을 것 같아서 가져옴.)
"""