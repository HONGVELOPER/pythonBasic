# 두 요소의 위치를 바꿔주는 helper function
def swap_elements(my_list, index1, index2):
    # 코드를 작성하세요.
    my_list[index1], my_list[index2] = my_list[index2], my_list[index1]

# 퀵 정렬에서 사용되는 partition 함수
def partition(my_list, start, end):
    # 코드를 작성하세요.
    pivot = my_list[end]
    # print(pivot)
    u = 0           # unknown
    b = 0           # big

    for i in my_list:
        if i == pivot:
            swap_elements(my_list, b, end)
            pivot = b
        elif i > pivot:
            u += 1
        else:
            swap_elements(my_list, b, u)
            u += 1
            b += 1
    
    return pivot


# 테스트 1
list1 = [4, 3, 6, 2, 7, 1, 5]
pivot_index1 = partition(list1, 0, len(list1) - 1)
print(list1)
print(pivot_index1)