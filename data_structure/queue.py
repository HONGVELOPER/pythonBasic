'''
Queue 한국말로는 대기열 이라고 한다.
다시 말해, 먼저 온 사람이 먼저 나간다는 뜻이다.
First In First Out (FIFO) 
'''

from collections import deque

queue = deque()

# 큐의 맨 끝에 데이터 삽입
queue.append('태호')
queue.append('현승')
queue.append('지웅')
queue.append('동욱')
queue.append('신의')

print(queue) # 큐 출력

# 큐의 맨 앞 데이터 접근
print(queue[0])

# 큐의 맨 앞 데이터 삭제 
print(f'{queue.popleft()} 가 제거 되었습니다.')
print(f'{queue.popleft()} 가 제거 되었습니다.')
print(f'{queue.popleft()} 가 제거 되었습니다.')

print(queue)

