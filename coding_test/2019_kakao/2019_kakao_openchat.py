record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234",
"Enter uid1234 Prodo","Change uid4567 Ryan"]

# 내가 푼거

def solution(record):
    answer = {}
    final = []
    for i in range(len(record)):
        record[i] = record[i].split(' ')
        if 'Leave' not in record[i]:
            answer[record[i][1]] = record[i][2]
    for i in range(len(record)):
        if 'Enter' in record[i]:
            final.append(f'{answer.get(record[i][1])}님이 들어왔습니다.')
        elif 'Leave' in record[i]:
            final.append(f'{answer.get(record[i][1])}님이 나갔습니다.')
    print(answer)
    print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
    print(final)
    return final

solution(record)

# --------------------------------------------ok-------------------------#

# 남이 푼거



