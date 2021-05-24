
def solution(s):
    answer = []
    final = []
    s = s[2:-2].split('},{')
    print(s)
    for i in s:
        a = [int(temp) for temp in i.split(',')]
        answer.append(a)
    print(answer)
    answer = sorted(answer, key=len)
    for i in answer:
        for j in i:
            if j not in final:
                final.append(j)
    print(final, 'final!')
    return final

s = "{{4,2,3},{3},{2,3,4,1},{2,3}}"
# s = "{{20,111},{111}}"
# s = "{{2},{2,1},{2,1,3},{2,1,3,4}}"

solution(s)