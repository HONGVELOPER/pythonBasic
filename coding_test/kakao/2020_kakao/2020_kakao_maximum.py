# expression = "100-200*300-500+20"
expression = "50*6-3*2"

import re
def solution(expression):
    answer = []
    priority = [['+', '-', '*'], ['+', '*', '-'], ['-', '+', '*'], ['-', '*', '+'], ['*', '+', '-'], ['*', '-', '+']]
    for i in priority:
        digit_list = list(map(int, re.compile('[0-9]+').findall(expression)))
        calculate_list = re.compile('[-,+,*]+').findall(expression)
        for j in i:
            while j == '+' and '+' in calculate_list:
                index = calculate_list.index('+')
                temp = digit_list[index] + digit_list[index+1]
                digit_list.pop(index)
                digit_list.pop(index)
                digit_list.insert(index, temp)
                calculate_list.pop(index)
            while j == '-' and '-' in calculate_list:
                index = calculate_list.index('-')
                temp = digit_list[index] - digit_list[index+1]
                digit_list.pop(index)
                digit_list.pop(index)
                digit_list.insert(index, temp)
                calculate_list.pop(index)
            while j == '*' and '*' in calculate_list:
                index = calculate_list.index('*')
                temp = digit_list[index] * digit_list[index+1]
                digit_list.pop(index)
                digit_list.pop(index)
                digit_list.insert(index, temp)
                calculate_list.pop(index)
        if len(digit_list) == 1:
            answer.append(abs(digit_list[0]))
    return max(answer)











    #     while i[0] in calculate_list:
    #         first = calculate_list.pop(calculate_list.index(i[0]))
    #         plus = digit_list[first] + digit_list[first+1]
    #     print('=============================')
    #     while i[0] in calculate_list and i[0] == '-':
    #         second = calculate_list.pop(calculate_list.index(j))
    #         plus = digit_list[first] + digit_list[first+1]
    #     print('=============================')
    #     while i[0] in calculate_list and i[0] == '+':
    #         first = calculate_list.pop(calculate_list.index(j))
    #         plus = digit_list[first] + digit_list[first+1]

solution (expression)



    