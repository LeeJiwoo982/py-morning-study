def score(txt):
    N = len(txt)
    result = 0
    now_score = 0

    for i in range(N):
        if txt[i] == 'O':
            now_score += 1
            result += now_score
        else:
            now_score = 0
    return result


T = int(input())
for tc in range(T):
    txt = input()
    print(score(txt))

"""
백준 링크:
https://www.acmicpc.net/problem/8958
"""