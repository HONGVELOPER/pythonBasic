def recur(n: int) -> int:
    '''순수한 재귀 함수 recur 구현'''
    if n > 0:
        recur(n - 1)
        print(n)
        recur(n - 2)

x = int(input('정숫값을 입력해주세요. :'))


recur(x)


'''함수 안에서 함수를 사용할 수 있다.'''