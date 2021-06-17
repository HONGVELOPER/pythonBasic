def solution(prices):
    answer = []
    for i in range(len(prices)):
        time = 0
        print(prices[i], '==============================')
        for j in range(i+1, len(prices)):
            print(j)
            print(prices[i], '|', prices[j])
            time += 1
            if prices[j] < prices[i]:
                break
        answer.append(time)
    print(answer)
    return answer

prices = [1, 2, 3, 2, 3]

solution(prices)