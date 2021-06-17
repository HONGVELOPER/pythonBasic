def solution(orders, course):
    dict = {}
    for one in orders:
        print(one)
        for i in one:
            # print(i)
            if i in dict:
                print('hi')
                dict[i] += 1
            else:
                dict[i] = 1
    print(dict)
    answer = []
    return answer




# orders = ["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"]
# orders = ["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"]
orders = ["XYZ", "XWY", "WXA"]
course = [2, 3, 4]

solution(orders, course)