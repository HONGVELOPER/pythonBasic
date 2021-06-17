def solution(maps):
    # end point에 도달할 수 없는 경우
    if maps[len(maps)-2][len(maps[0])-1] == 0 and maps[len(maps)-1][len(maps[0])-2] == 0:
        return -1
    else:
        row = 0
        col = 0
        count = 1
        recent = None
        while row != len(maps)-1 and col !=len(maps[0]):
            if maps[row+1][col] == 1 and recent != 'up':
                recent = 'down'
                row += 1
                count += 1
                print(row, '|',  col, 'down')
            elif maps[row][col+1] == 1 and recent != 'left':
                recent = 'right'
                col += 1
                count += 1
                print(row, '|',  col, 'right')
            elif maps[row-1][col] == 1 and recent != 'down':
                recent = 'up'
                row -= 1
                count += 1
                print(row, '|',  col, 'up')
            elif maps[row][col-1] == 1 and recent != 'right':
                recent = 'left'
                col -= 1
                count += 1
                print(row, '|',  col, 'left')
        return count
            







maps = [[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]
# maps = [[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,0],[0,0,0,0,1]]
print(solution(maps))

# 다시ㅣㅣㅣㅣㅣㅣㅣㅣㅣㅣㅣㅣㅣㅣ BFS 공부해ㅐㅐㅐㅐㅐㅐㅐㅐㅐㅐ