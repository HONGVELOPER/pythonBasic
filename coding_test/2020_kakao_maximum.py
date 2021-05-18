expression = "100-200*300-500+20"
# expression = "50*6-3*2"
def solution(expression):
    array = [['+', '-', '*'], ['+', '*', '-'], ['-', '+', '*'], ['-', '*', '+'], ['*', '+', '-'], ['*', '-', '+']]
    final = []
    for i in array:
        for j in i:
            id = expression.find(j)
            bef = expression[:id].rfind('+' or '-' or '*')
            print(id)
            print(bef)
            break
        break
    #         if j == '+':
    #             result = int(expression[id-1]) + int(expression[id+1])
    #         elif j == '-':
    #             result = int(expression[id-1]) - int(expression[id+1])
    #         else:
    #             result = int(expression[id-1]) * int(expression[id+1])
    #         expression = expression.replace(expression[id-1:id+2], str(result))
    #     final.append(int(expression))
    # biggest = max(final)

solution (expression)



    