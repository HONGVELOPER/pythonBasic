

board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
moves = [1,5,3,5,1,2,1,4]


def solution(board, moves):
    bag = []
    answer = 0
    ptr = 0
    moves = list(map(minus, moves))
    for i in moves:
        for j in range(0, len(board[0])):
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

