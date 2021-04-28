from typing import MutableSequence
'''
버블 정렬에서 교환횟수가 0이라는 뜻은 이 후에는 정렬이 이미 되었다 라는 뜻으로
후에는 정렬을 하지 않고 함수를 종료시키기 위한 exchange 변수를 선언햇다.
'''

def buble_sort(a: MutableSequence) -> None:

    n = len(a)
    for i in range(n - 1):
        exchange = 0
        for j in range(n - 1, i, -1):
            if a[j - 1] > a[j]:
                a[j - 1], a[j] = a[j], a[j - 1]
                exchange += 1
        if exchange == 0:
            break
    