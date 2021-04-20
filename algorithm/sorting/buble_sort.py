'''
버블 정렬은 이웃한 두 원소의 대소 관계를 비교하여 필요에 따라 교환으 반복하는
알고리즘으로, 단순 교환 정렬이라고 한다.
'''

# list = [6, 4, 3, 7, 1, 9, 8]

# for i in list:
#     # print(i)
#     for i+1 in list:
#         print(i)  



#-----------------------------------------------------------------------------#  


from typing import MutableSequence

def buble_sort(a: MutableSequence) -> None:
    ''' 버블 정렬 '''
    n = len(a)
    for i in range(n - 1):
        for j in range(n - 1, i, -1):
            if a[j - 1] > a[j]:
                a[j - 1], a[j] = a[j], a[j - 1]

if __name__ == '__main__':
    print('버블 정렬을 수행합니다. ')
    num = int(input('원소 수를 입력해주세요. '))

    x = [None] * num

    for i in range(num):
        x[i] = int(input(f'x[{i}] : '))

    buble_sort(x)

    print('오름차순으로 정렬했습니다.')

    for i in range(num):
        print(f'x[{i}] = {x[i]}')    