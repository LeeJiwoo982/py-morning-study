from collections import deque
import sys
sys.stdin = open('input.txt', 'r')

T = 10
for tc in range(1, T+1):
    input()

    N = list(map(int, input().split()))

    queue = deque(N)    #큐 활용   큐에 전부 넣기
    decrement = 1   #감소는 1부터

    while True:
        num = queue.popleft() - decrement   #첫번째 숫자 감소
        if num <=0: #0보다 작아지면 0으로 설정 후 종료
            queue.append(0)
            break
        queue.append(num)

        decrement = decrement % 5 + 1   #감소 값 1, 2, 3, 4, 5 반복

    # result = ' '.join(map(str, queue))
    print(f'#{tc} {" ".join(map(str, queue))}')