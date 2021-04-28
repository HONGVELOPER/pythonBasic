from collections import deque

queue = deque([4, 5, 6])
queue.append(7)
queue.append(8)

print(queue)

queue.popleft() # 왼쪽에서 pop

print(queue)

queue.pop() # 오른쪽에서 pop