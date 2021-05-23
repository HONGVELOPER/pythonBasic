def merge(list1, list2):
    sum_array = []
    while len(list1) >= 1 and len(list2) >= 1:
        if list1[0] > list2[0]:
            sum_array.append(list2.pop(0))
        else:
            sum_array.append(list1.pop(0))
    if len(list1) == 0 and len(list2) > 0:
        sum_array.extend(list2)
    elif len(list2) == 0 and len(list1) > 0:
        sum_array.extend(list1)
    return sum_array

# print(merge([1],[]))
# print(merge([],[1]))
# print(merge([2],[1]))
# print(merge([1, 2, 3, 4],[5, 6, 7, 8]))
# print(merge([5, 6, 7, 8],[1, 2, 3, 4]))
# print(merge([4, 7, 8, 9],[1, 3, 6, 10]))

def merge_sort(my_list):
    # 코드를 입력하세요.
    # mid = (0 + len(my_list) // 2)
    if len(my_list) < 2:
        return my_list
    left = merge_sort(my_list[:len(my_list) // 2])
    right = merge_sort(my_list[len(my_list) // 2:])
    return merge(merge_sort(left), merge_sort(right))

print(merge_sort([1, 3, 5, 7, 9, 11, 13, 11]))
print(merge_sort([28, 13, 9, 30, 1, 48, 5, 7, 15]))
print(merge_sort([2, 5, 6, 7, 1, 2, 4, 7, 10, 11, 4, 15, 13, 1, 6, 4]))