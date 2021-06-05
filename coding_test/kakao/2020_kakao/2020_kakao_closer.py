# numbers = [3, 30, 34, 5, 9]
numbers = [6, 10, 2]

def solution(numbers):
    numbers = list(map(str, numbers))
    print(numbers, 'numbers')
    numbers.sort(key=lambda x: x[0], reverse=True)
    return str(int(''.join(numbers)))
print(solution(numbers))