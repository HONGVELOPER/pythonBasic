'''
stack 이란 접시쌓기 와 같다고 생각하자
닦은 접시는 위에 넣고, 음식이 나갈때도 위에 있는 접시로 먼저 나간다.
Last In First Out (LIFO)
'''

from collections import deque

stack = deque()

stack.append('T')
stack.append('A')
stack.append('E')
stack.append('H')
stack.append('O')

print(stack)

# 맨 끝 데이터 접근
print(stack[-1])


# 맨 끝 데이터 삭제
print(f'{stack.pop()} 제거 되었습니다.')
print(f'{stack.pop()} 제거 되었습니다.')
print(f'{stack.pop()} 제거 되었습니다.')

print(stack)