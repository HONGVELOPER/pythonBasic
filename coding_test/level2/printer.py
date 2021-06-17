def solution(priorities, location):

    count = 0
    while priorities: 
        front = 0
        copy = front
        for i in range(1, len(priorities)):
            if priorities[i] > priorities[front]:
                if location == 0:
                    location = len(priorities) - 1
                else:
                    location -= 1 
                priorities.append(priorities[front])
                priorities.pop(front)
                front = i
                break
        if front == copy:
            priorities.pop(0)
            count += 1
            if location == 0:
                return count
            else:
                location -= 1    
    

priorities = [2, 1, 3, 2]
location = 2
# priorities = [1, 1, 9, 1, 1, 1]
# location = 0
print(solution(priorities, location))