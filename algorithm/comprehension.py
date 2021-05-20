# # for문 comprehension

# a = [x for x in range(10)]
# # print(a)

# # if문 comprehension

# b = [x for x in range(10) if x % 2 ==0]
# # print(b)

# c = [(y, z) for y in range(10) for z in range(10) ]
# # print(c)

# d = [z for z in range(10) if z % 2 == 0 if z > 5]
# # print(d)

# f = 1
# e = 1 if f % 2 == 0 else -1
# print(e)


# def check_comprehension():
#     numbers = []
#     for n in range(1, 11):
#         numbers.append(n)
#     print(numbers)

def check_comprehension():
    numbers = [x for x in range(1, 11) if x % 2 == 0]
    print(numbers)


check_comprehension()