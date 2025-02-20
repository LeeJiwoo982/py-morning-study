def cal1(N, txt):
    stack = [0]*N
    idx = -1
    result = ''
    for t in txt:
        if t.isdecimal():
            result += t
        else:
            if idx<0:
                idx+=1
                stack[idx] = t
            else:
                idx -= 1
                result += stack[idx+1]
                idx += 1
                stack[idx] = t
    result += stack[idx]
    idx -= 1

    result = cal2(result)
    return result


def cal2(result):
    stack = [0] * len(result)
    idx = -1
    for t in result:
        if t.isdecimal():
            idx += 1
            stack[idx] = int(t)
        else:
            B = stack[idx]
            idx -= 1
            A = stack[idx]
            idx -= 1
            if t == '+':
                idx += 1
                stack[idx] = A+B
    return stack[idx]


for tc in range(1, 11):
    N = int(input())
    txt = input()
    print(f"#{tc} {cal1(N, txt)}")