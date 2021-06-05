import math
def solution(w, h):
    answer = w * h
    count = 0
    prev = 0.0
    value = w / h
    for _ in range(h):
        if len(str(prev).split('.')[1]) > 5 and str(prev).split('.')[1][:5] == '99999':
            prev += 0.1
        count = math.ceil(value) - math.floor(prev)
        answer -= count
        prev = value
        value = value + (w / h)
    return answer
    # print(answer)

solution(8, 12)



# retry 뭐가 문제인지를 모르겠는게 문제다 아ㅏㅏㅏㅏㅏㅏㅏㅏㅏㅏㅏㅏㅏㅏㅏㅏㅏ