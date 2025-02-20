def forth(val):
    global result
    stack=[0]*len(val)
    idx = -1
    for n in val:
        if n.isdecimal():
            idx+=1
            stack[idx] = int(n)
            # print(stack)
        else:
            if n == '.':
                if idx==0:
                    result = stack[idx]
                return
            b = int(stack[idx])
            idx -= 1
            a = int(stack[idx])
            idx -= 1
            if n == '+':
                idx+=1
                stack[idx] = a+b
            elif n == '*':
                idx+=1
                stack[idx] = a*b
            elif n == '-':
                idx+=1
                stack[idx] = a-b
            elif n == '/':
                idx+=1
                stack[idx] = a//b
            # print(stack)
    pass


T = int(input())
for tc in range(1, T+1):
    val = input().split()
    result = 'error'
    forth(val)
    print(f"#{tc} {result}")