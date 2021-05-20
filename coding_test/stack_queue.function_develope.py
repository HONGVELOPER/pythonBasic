from collections import deque
from math import ceil

def solution(progresses, speeds):
    queue = deque()
    answer = []
    guage_bar = []

    queue = [i for i in progresses]
    for i in range(len(queue)):
        a = (100 - queue[i]) / speeds[i]
        if '.' in str(a):
            a = ceil(a)
            guage_bar.append(a)
    print(guage_bar)

    # iterator = 0
    # while iterator is not None:
    #     for i in guage_bar:
    #         print(i, '번째')
    #         if guage_bar[iterator] >= i:
    #             guage_bar.popleft()
    #             print(guage_bar)


    forbreak = False
    for i in guage_bar[:]:
        count = 0
        for j in guage_bar:
            print(len(guage_bar) ,count)
            if i >= j:
                count += 1
            else:
                print(count, 'count')
                guage_bar = guage_bar[count:]
                break
        print(guage_bar.count(guage_bar[0]), 'check')
        # if guage_bar.count(guage_bar[0]) == len(guage_bar) and not forbreak:
        #     print('here?')
        #     answer.append(count)
        #     forbreak = True
        if count and forbreak == False:
            answer.append(count)
    print(answer)

solution([90, 90, 90], [5, 5, 5])
# solution([93, 30, 55], [1, 30, 5])
# solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1])

'''
guage bar queue 에서 뒤에 있는게 값이 더 클때까지 pop 하기

'''