import sys
sys.stdin = open('input.txt', 'r')

N = int(input())

for i in range(1,11):
    if N % i == 0:
        # N = N / i
        print(i, end = ' ')