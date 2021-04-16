def solution(x):
    a = []
    for i in str(x):
        a.append(i)
        print(a)

    b = sum(map(int, a))
        
    if x % b == 0:
        answer = True
    else:
        answer = False
    return answer

if __name__ == '__main__':
    solution(12)
