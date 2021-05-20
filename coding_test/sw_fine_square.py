w = 8
h = 12

import math
def solution(w,h):
    answer = 0
    if h > w:
        w, h = h, w
    left = 0
    right = w / h
    for _ in range(h):
        print(left, right, math.ceil(right) - int(left))
        answer += (math.ceil(right) - math.floor(left))
        left = right
        right += w / h
    # return w * h - answer
    print(w * h - answer)


solution(w, h)

#failllllllllllllllllllllllllllllllllllllllllllll