def kmp_mine(str, pat):
    table = [0]
    tp = 0
    pp = 0
    pt = 0

    for i in pat[1:]:
        if i == pat[tp]:
            tp += 1
            table.append(tp)
        else:
            tp = 0
            table.append(0)
    print(table)

    while pp != len(pat):
        if str[pt] == pat[pt]:
            pt += 1
            pp += 1
        else:
            if str[pt] in pat:
                pt = table[pp]
            else:
                pt = pt - pp + 1
            pp = 0
    print(f'찾고자 하는 값이 {pt - pp} 번째 index 부터 시작합니다.')

        

kmp_mine('asdaabcabde', 'abcabd')