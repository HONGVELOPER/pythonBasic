def solution(s):
    stk = []
    for i in s:
        if len(stk) == 0:
            stk.append(i)
        elif i == stk[-1]:
            stk.pop()
        else:
            stk.append(i)
    if len(stk) == 0:
        return 1
    else:
        return 0

s = 'baabaa'
print(solution(s), 'result')