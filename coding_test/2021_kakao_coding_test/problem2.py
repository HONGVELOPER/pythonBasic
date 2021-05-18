# places = [["PXOPX", "OXOXP", "OXPXX", "OXXXP", "POOXX"], ["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"],  ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]

places= [["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]
def solution(places):
    person = []
    problem = []
    count = False
    if 'P' not in places[0]:
        count = True
    for i in places[0]:
        idx = 0
        idx_count = 0
        for j in i:
            if j == 'P':
                print(j, places[0].index(i), i[idx:].find('P') + idx_count)
                person.append((places[0].index(i), i[idx:].find('P') + idx_count))
                idx = i.find('P')
            idx_count += 1
            
    print(person, 'person')
    for i in range(len(person)):
        for j in person[i+1:]:
            print(person[i], j)
            if (abs(person[i][0] - j[0]) + abs(person[i][1] - j[1])) > 2:
                count = True
            else:
                problem.append((person[i], j))
    print(problem, 'problem')
    if len(problem) > 0:
        for i in problem:
            print(i, 'iiiiiii')
            a = [(i[1][0] + i[0][0]) / 2, (i[1][1] + i[0][1]) / 2]
            if a[0] % 2 == 0 and a[1] != 0.0:
                a[0], a[1] = int(a[0]), int(a[1])
                if places[0][a[0]][a[1]] == 'X':
                   print('ok1')
                   count = True
                else:
                    count = False
            elif a[1] % 2 == 0 and a[0] != 0.0:
                a[0], a[1] = int(a[0]), int(a[1])
                if places[0][a[0]][a[1]] == 'X':
                   print('ok2')
                   count = True
                else:
                    count = False
            else:
                if places[0][i[0][0]][i[1][1]] == 'X' and places[0][i[0][1]][i[1][0]] == 'X':
                    print('ok3')
                    count = True
                else:
                    print(i[0][0], i[1][1], i[0][1], i[1][0], 'check')
                    count = False
    if count:
        print('hi', count)
    else:
        print('fail', count)
            
            # print(i[0])
            # print(i[1])
    answer = []
    return answer



solution(places)