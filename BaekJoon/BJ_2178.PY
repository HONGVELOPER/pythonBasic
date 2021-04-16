# row = int(input('row : '))
# col = int(input('col : '))

# darray = [r

# x = 0
# y = 0
# count = 0

# right = True
# left = True
# up = True
# down = True

# print(darray)

# def move_right(x, y):
#     if darray[x][y + 1] == 1:
#         y = y + 1
#         count += 1
#         previous_move(right)
#         left, up, down = True
#     return darray[x][y + 1] == 1

# def move_down(x, y):
#     if daaray[x+1][y] == 1:
#         x = x + 1
#         count += 1
#         previous_move(down)
#         right, left, up = True
#     return darray[x + 1][y] == 1

# def move_left(x, y):
#     if darray[x][y-1] == 1:
#         y = y - 1
#         count -= 1
#         previous_move(left)
#         right, up, down = True
#     return darray[x][y-1] == 1

# def move_up(x, y):
#     if darray[x-1][y] == 1:
#         x = x - 1
#         count -= 1
#         previous_move(up)
#         right, left, down = True
#     return darray[x-1][y] == 1

# def previous_move(pre):
#     if pre == right:
#         right = false
#         return right

#     if pre == left:
#         left = False
#         return left

#     if pre = up:
#         up = False
#         return up
    
#     if pre = down:
#         down = False
#         return down

# def move(x, y):
#     if move_right() and right:
#         move_right()
#     elif move_down() and down:
#         move_down()
#     elif move_left() and left:
#         move_left()
#     elif move_up() and up:
#         move_up()
    