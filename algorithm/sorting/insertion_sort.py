'''

단순 삽입 정렬
주목한 원소보다 더 앞쪽에서 알맞은 위치로 삽입하여 정렬하는 알고리즘
단순 선택 정렬과 비슷해 보이지만, 값이 가장 작은 원소를 선택하지 않는다는 점이 다름.

'''

from typing import MutableSequence

def insertion_sort(a: MutableSequence) -> None:

    n = len(a)
    for i in range(1, n):
        j = iw
        tmp = a[i]
        while j > 0 and a[j - 1] > tmp:
            a[j] = a[j - 1]
            j -= 1

        a[j] = tmp

if __name__ =='__main__':
    print('단순 삽입 정렬을 수행합니다. ')
    num = int(input('원소 수를 입력해주세요. :'))
    x = [None] * num

    for i in range(num):
        x[i] = int(input(f'x[{i}]: '))

    insertion_sort(x)

    print('오름 차순으로 정렬되었습니다.')
    for i in range(num):
        print(f'x[{i}] = {x[i]}')