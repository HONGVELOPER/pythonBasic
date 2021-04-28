from typing import MutableSequence

def buble_sort(a: MutableSequence) -> None:

    n = len(a)
    k = 0

    while k < n - 1:
        last = n - 1 
        for j in range(n -1, k, -1):
            if a[j - 1] > a [j]:
                a[j - 1], a[j] = a[j], a[j -1]
                last = j # 교환이 발생한 마지막 index 를 last에 저장
        k = last