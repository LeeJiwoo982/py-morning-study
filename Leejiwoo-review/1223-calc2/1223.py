import sys
sys.stdin = open('input.txt', 'r')

def infix_to_postfix(expression):
    '''중위를 후위로 변환'''
    precedence = {'+':1, '-':1, '*':2, '/':2}   #연산자 우선순위
    output = [] #결과식
    stack = []  #연산자 스택

    for char in expression:
        if '0' <= char <= '9':
            output.append(char)
        elif char in precedence:
            while stack and precedence.get(stack[-1], 0) >= precedence[char]:
                output.append(stack.pop())  #스택에서 연산자 꺼내 결과식에 추가
            stack.append(char)  #현재 연산자
    while stack:    #스택에 연산자가 남아 있으면
        output.append(stack.pop())

    return ''.join(output)

def evaluate_postfix(postfix):
    '''후위표기식 계산'''
    stack = []

    for char in postfix:
        if '0'<=char<='9':
            stack.append(int(char))
        else:
            b = stack.pop()
            a = stack.pop()
            if char == '+':
                stack.append(a+b)
            elif char == '-':
                stack.append(a-b)
            elif char == '*':
                stack.append(a*b)
            # elif char == '/': #이번 문제는 *와 +만 있음
            #     stack.append(a//b)

    return stack[0]

T = 10
for tc in range(1, T+1):
    N = int(input())
    infix= list(input())

    postfix = infix_to_postfix(infix)
    result = evaluate_postfix(postfix)

    print(f'#{tc} {result}')