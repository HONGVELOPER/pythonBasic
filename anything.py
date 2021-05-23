# def trapping_rain(buildings):
#     total = 0
#     print(buildings[1:len(buildings) - 1])
#     for i in buildings[1:len(buildings) - 1]:
#         left_max = max(buildings[:buildings.index(i)])
#         right_max = max(buildings[buildings.index(i):])
#         print(left_max, right_max)
#         total += min(left_max, right_max) - i
#     return total
        
#         # right_max = max(buildings[i+1:])
#         # real_max = max(left_max, right_max)
#         # print(real_max)

# # 테스트
# print(trapping_rain([0, 3, 0, 0, 2, 0, 4]))

a = [1, 2, 3]
b = a
print(id(a))
print(id(b))
a = [4 ,5]
print(id(a))
print(id(b))
# print(a, b)