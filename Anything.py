a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for i in a:
    print('=====================')
    if i % 2 == 0:
        if i == 4:
            continue
            print('check')
        print('짝수', i)
    print('hey')
    if i % 2 != 0:
        print('홀수', i)

