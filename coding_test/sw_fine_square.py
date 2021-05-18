w = 3
h = 12

import math
def solution(w,h):
    answer = 0
    if (h > w):
        w, h = h, w
    a = w / h
    left = 0
    right = w / h
    for _ in range(h):
        answer += (math.ceil(right) - math.floor(left))
        left = right
        right += a
    # return w * h - answer
    print(w * h - answer)


solution(w, h)

#failllllllllllllllllllllllllllllllllllllllllllll