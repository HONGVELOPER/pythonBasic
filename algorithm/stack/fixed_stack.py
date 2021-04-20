from typing import Any

class FixedStack:
    
    class Empty(Exception):
        pass

    class Full(Exception):
        pass

    def __init__(self, capacity: int = 256) -> None:
        self.stk = [None] * capacity
        self.capacity = capacity
        self.ptr = 0


    def __len__(self) -> int:
        return self.ptr


    def is_empty(self) -> bool:
        return self.ptr <= 0

    def is_full(self) -> bool:
        return self.ptr >= self.capacity

    def push(self, value: Any) -> None:
        ''' 스택에 value 푸쉬함 '''
        if self.is_full(): # 스택이 가득 차 있는 경우
            raise FixedStack.Full # 예외처리 발생

        self.stk[self.ptr] = value
        self.ptr += 1

    def pop(self) -> Any:
        if self.is_empty():
            raise FixedStack.Empty

        self.ptr -= 1
        return self.stk[self.ptr]

    def peek(self) -> Any:
        if self.is_empty():
            raise FixedStack.Empty

        return self.stk[self.ptr -1]

    def clear(self) -> None:
        self.ptr = 0

    def find(self, value: Any) -> Any:
        for i in range(self.ptr - 1, -1, -1):
            if self.stk[i] == value:
                return i
        return -1

    # 스택에 value의 값을 갖고 있는 원소의 개수를 return
    def count(self, value: Any) -> Any:
        c = 0
        for i in range(self.ptr):
            if self.stk[i] == value:
                c += 1
        return c

    def dump(self) -> None:
        if self.is_empty():
            print('스택이 비엇습니다.')
        else:
            print(self.stk[:self.ptr])