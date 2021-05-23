def solution(progresses, speeds):

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

# print(solution([93, 30, 55], [1, 30, 5]))
# print(solution([90, 90, 90], [5, 5, 5]))
print(solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]))
