import sys
sys.stdin = open('sample_input.txt', 'r')

def winner(a, b):
    '''플레이어 a, b 중 승자를 반환'''
    idx_a, card_a = a
    idx_b, card_b = b

    #같은 번호면 번호가 작은 사람 승
    if card_a == card_b:
        return a if idx_a < idx_b else b

    # 가위1 > 바위3, 바위2>가위1, 보3>바위2
    if (card_a == 1 and card_b==3) or (card_a == 2 and card_b==1) or (card_a == 3 and card_b == 2):
        return a
    return b

T= int(input())
for tc in range(1, T+1):
    N = int(input()) #인원수
    arr = list(map(int, input().split()))

    stack = [(i+1, arr[i]) for i in range(N)] #학생번호, 카드 저장

    while len(stack)>1:
        temp_stack = [] #다음 라운드 스택

        while len(stack)>1:
            player1 = stack.pop(0)
            player2 = stack.pop(0)
            temp_stack.append(winner(player1, player2))

        #홀수명은 마지막 남은 사람 다음 라운드 추가
        if stack:
            temp_stack.append((stack.pop()))

        stack = temp_stack #스택 갱신

    print(f'#{tc} {stack[0][0]}')