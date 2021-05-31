expression = "100-200*300-500+20"
# expression = "50*6-3*2"

import re
def solution(expression):
    priority = [['+', '-', '*'], ['+', '-', '*'], ['-', '+', '*'], ['-', '*', '+'], ['*', '+', '-'], ['*', '-', '+']]
    answer = 0
    digit_list = re.compile('[0-9]+').findall(expression)
    calculate_list = re.compile('[-,+,*]+').findall(expression)
    for i in priority:
        while i[0] in calculate_list:
            printi[0]
            first = calculate_list.pop(calculate_list.index(i[0]))
            plus = digit_list[first] + digit_list[first+1]
        print('=============================')
        while i[0] in calculate_list and i[0] == '-':
            second = calculate_list.pop(calculate_list.index(j))
            plus = digit_list[first] + digit_list[first+1]
        print('=============================')
        while i[0] in calculate_list and i[0] == '+':
            first = calculate_list.pop(calculate_list.index(j))
            plus = digit_list[first] + digit_list[first+1]


solution (expression)



    