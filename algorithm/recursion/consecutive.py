# def consecutive_sum_mine(start, end):
#     sum = 0
#     if end//2 > start:
#         a = consecutive_sum(start, end // 2)
#         b = consecutive_sum(end // 2 + 1, end)
#         sum = sum + a + b
#     else:
#         for i in range(end - start + 1):
#             sum += start + i 
#     return sum

def consecutive_sum(start, end):
    if end == start:
        return start
    
    mid = (start + end) // 2
    return consecutive_sum(start, mid) + consecutive_sum(mid + 1, end)


# # 테스트
# print(consecutive_sum(1, 10))