def solution(board, moves):
    bag = []
    answer = 0
    ptr = 0
    moves = list(map(minus, moves))
    for i in moves:
        for j in range(len(board[0])):
            if board[j][i] != 0:
                if ptr == 0:
                    bag.append(board[j][i])
                    ptr += 1
                    board[j][i] = 0
                    break
                elif bag[ptr-1] == board[j][i]:
                    answer += 2
                    # ptr -= 1
                    del bag[ptr - 1]
                    ptr -= 1
                    board[j][i] = 0
                    break
                else:
                    bag.insert(ptr, board[j][i])
                    ptr += 1
                    board[j][i] = 0
                    break
    return answer

def minus(a):
    return a - 1

solution(board, moves)

def solution_other(board, moves):
    stacklist = []
    answer = 0

    for i in moves:
        for j in range(len(board)):
            if board[j][i-1] != 0:
                stacklist.append(board[j][i-1])
                board[j][i-1] = 0
            
                if len(stacklist) > 1:
                    if stacklist[-1] == stacklist[-2]:
                        stacklist.pop(-1)
                        stacklist.pop(-1)
                        answer += 2
                break
    return answer
