s = "one4seveneight"

def solution(s):
    all = [(0, 'zero'), (1, 'one'), (2, 'two'), (3, 'three'), (4, 'four'), (5, 'five'), (6, 'six'), (7, 'seven'), (8, 'eight'), (9, 'nine')]
    for i in all:
        where = 0
        while s[where:].find(i[1]) != -1:
            idx = s.find(i[1])
            where = idx + 1
            s = s.replace(s[idx : idx + len(i[1])], str(i[0]))
    s = int(s)
    return s


solution(s)