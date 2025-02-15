def dwarf(arr):
    for i in range(1<<9):
        part = []
        for j in range(9):
            if i&(1<<j):
                part.append(arr[j])
        if len(part)==7 and sum(part) == 100:
            part.sort()
            for n in range(7):
                print(part[n])
            return None


arr = [0]*9
for i in range(9):
    arr[i] = int(input())
dwarf(arr)

"""
백준 링크:
https://www.acmicpc.net/problem/2309
뭔가... 2의 9승이어서 부분집합 풀어도 됐는데, 훨씬 경우의 수 자체는 적어서 아쉽다... 
줄일 방법이 없나?
"""

