def swap_elements(my_list, index1, index2):
    # 코드를 작성하세요.
    my_list[index1], my_list[index2] = my_list[index2], my_list[index1]

# 퀵 정렬에서 사용되는 partition 함수
def partition(my_list, start, end):
    # 코드를 작성하세요.
    pivot = my_list[end]
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
    
# 퀵 정렬
# sort_array = []
def quicksort(my_list, start, end):
    # 코드를 작성하세요
    if end - start < 1:     # start 와 end 가 같이 있거나, start 가 end 보다 값이 클경우 err
        return
    
    pivot = partition(my_list, start, end)

    quicksort(my_list, start, pivot - 1)
    quicksort(my_list, pivot + 1, end)

# 테스트 1
# list1 = [1, 3, 5, 7, 9, 11, 13, 11]
list1 = [28, 13, 9, 30, 1, 48, 5, 7, 15]
quicksort(list1, 0, len(list1) - 1)
print(list1)