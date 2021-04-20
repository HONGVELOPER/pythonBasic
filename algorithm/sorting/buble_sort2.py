# 버블 정렬 알고리즘 구현하기 (정렬 과정 출력)

from typing import MutableSequence

def buble_sort_verbose(a: MutableSequence) -> None:
    
    ccnt = 0
    scnt = 0

    n = len(a)

    for i in range(n - 1):
        print(f'패스 {i + 1}')
        for m in range(n - 1, i, -1):
            for m in range(0, n, -1):
                print(f'{a[m]:2' +)