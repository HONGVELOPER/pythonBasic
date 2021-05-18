# print((lambda x: x + 10)(1))


# for i, value in enumerate(([1, 2, 3])):
#     print(i, value)


# a = [(1, 2), (0, 1), (5, 1), (5, 2), (3, 0)]
# print(sorted(a, key = lambda x : x[0]))

a = [5, 2, 3, 1, 4]
# print(sorted(a))
# sorted(a)
# a.sort()
# print(a)

'''
sorted vs sort

sorted 는 리스트를 정렬시키며 새로운 list 를 생성하는 반면
sort 는 해당 리스트를 재정렬 시키는 것에 의미가 있다

다시 말해, sorted 는 새로운 list 를 만들어 있던 원래 list 에 영향을 주지 않아
2개의 배열이 모두 필요할 경우에 사용하는것이 좋다.

정렬 전 list 가 필요하지 않을경우에는 sort() 를 사용하는것이 좋다.
'''