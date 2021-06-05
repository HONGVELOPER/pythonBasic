# 가장 인기 있는 풀이
'''
# def solution(progresses, speeds):

    answer = []
    day = 0     # 소요된 날짜
    count = 0   # 하루에 배포되는 서비스 개수
    while progresses:               #progresses 가 빈 리스트가 아닐경우          
        if (progresses[0] + day * speeds[0]) >= 100:
            progresses.pop(0)
            speeds.pop(0)
            count += 1
        else:
            if count > 0:           #  
                answer.append(count)
                count = 0
            day += 1
    answer.append(count)
    return answer
'''

# progresses = [93, 30, 55]
progresses = [95, 90, 99, 99, 80, 99]
# speeds = [1, 30, 5]
speeds = [1, 1, 1, 1, 1, 1]

# 내 풀이
def solution(progresses, speeds):
    day = 0
    answer = []
    while progresses:
        if progresses[0] + (day * speeds[0]) < 100:
            day += 1
        else:
            count = 0
            while progresses:
                if progresses[0] + (day * speeds[0]) < 100:
                    break
                progresses.pop(0)
                speeds.pop(0)
                count += 1
            answer.append(count)
            if len(progresses) == 0:
                return answer
            day = 0


print(solution(progresses, speeds))