# 단순 선택 정렬

from typing import MutableSequence

a = [3, 4, 2, 3, 1]
def selection_sort(a: MutableSequence) -> None:

    n = len(a)
    for i in range(n - 1):
        min = i
        for j in range(i + 1, n):
            if a[j] < a[min]:
                min = j

        a[i], a[min] = a[min], a[i]
    
    print(a)

selection_sort(a)
'''
 이 알고리즘은 안정적이지는 않다.
 예를들어 3이 2개 일때 왼쪽 3을 3(LEFT) 오른쪽 3을 3(RIGHT)라 할 때,
 이 3의 위치가 바뀔 수 있기 때문이다.

 ea) 3(left) 4 2 3(right) 1 일경우

    1 4 2 3(right) 3(left)
    1 2 4 3(right) 3(left)
    1 2 3(rignt) 4 3(left)
    1 2 3(right) 3(left) 4
    
    순으로 바뀔 수 있다. 
    즉, 중복된 값으로 정렬이 필요 없는 데이터의 위치가 바뀌었다는 뜻이다.
'''