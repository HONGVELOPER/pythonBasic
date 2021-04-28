# numbers = [6, 10, 2]
numbers = [3, 30, 34, 5, 9]

def solution(numbers):
    answer = []
    # n = len(numbers) - 1
    biggest = 0
    for i in range(len(numbers) - 1):
        n =[]
        for j in numbers:
            if len(str(j))-1 == i:
                n.append(j)
                print('진입')
        answer.append(n)    
        answer.sort(reverse=True)
        if 
    print(answer)
    # biggest = max(answer)

solution(numbers)


# fail~~~~~~~~~~~~~