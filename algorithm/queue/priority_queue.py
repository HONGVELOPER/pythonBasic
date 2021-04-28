from queue import priorityqueue

que = PriorityQueue(maxsize=8)

que.put(4)
que.put(1)
que.put(7)
que.put(3)

print(que.get())


