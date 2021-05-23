# numbers = [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]
# numbers = [7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2]
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
numbers = [0]
# hand = 'right'
hand = 'right'

def solution(numbers, hand):
    print('start')
    answer = ''
    now_left = 10
    now_right = 12 
    for i in numbers:
        if i == 0:
            i = 11
        if i == 1 or i == 4 or i == 7:
            answer = answer + 'L'
            now_left = i
        elif i == 3 or i == 6 or i == 9:
            answer = answer + 'R'
            now_right = i
        else:
            next = 0
            left = 0
            right = 0
            length = [[1,2,3],[4,5,6],[7,8,9],[10,11,12]]
            for j in range(len(length)):
                for k in range(len(length[0])):
                    if length[j][k] == i:
                        next = j, k
                    if length[j][k] == now_left:
                        left = j, k
                    if length[j][k] == now_right:
                        right = j, k
            if (abs(next[0] - left[0]) + abs(next[1] - left[1])) > (abs(next[0] - right[0]) + abs(next[1] - right[1])): 
                answer = answer + 'R'
                now_right = i
            elif (abs(next[0] - left[0]) + abs(next[1] - left[1])) < (abs(next[0] - right[0]) + abs(next[1] - right[1])):
                answer = answer + 'L'
                now_left = i
            else:
                if hand == 'left':
                    answer = answer + 'L'
                    now_left = i
                else:
                    answer = answer + 'R'
                    now_right = i
    print(answer)
    return answer


solution(numbers, hand)
