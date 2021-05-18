n = 8 # 표의 행 개수
k = 2 # 처음 행을 가리키는 포인터 위치
cmd = ["D 2","C","U 3","C","D 4","C","U 2","Z","Z"]
# cmd = ["D 2","C","U 3","C","D 4","C","U 2","Z","Z","U 1","C"]
def solution(n, k, cmd):
    answer = ''
    name = ''
    delete = []
    a = []
    
    a.append([0, '무지'])
    a.append([1, '콘'])
    a.append([2, '어피치'])
    a.append([3, '제이지'])
    a.append([4, '프로도'])
    a.append([5, '네오'])
    a.append([6, '튜브'])
    a.append([7, '라이언'])
    copy = a[:]
    name = a[k][1]
    print(name)
    for i in cmd:
        if 'U' in i:
            k -= int(i[2])
            name = a[k][1]
            print(name, 'U')
        elif 'D' in i:
            k += int(i[2])
            name = a[k][1]
            print(name, 'D')
        elif 'C' in i:
            delete.append(a[k])
            print('삭제 된 것', delete, k)
            del a[k]
            if len(a) - 1 == k:
                k -= 1
            for i in a:
                if i[0] > k:
                    i[0] -= 1
            print(a, k, 'kkkk')
        elif 'Z' in i:
            re = delete.pop()
            print(re[1], '복귀')
            for i in a:
                if i[0] >=  re[0]:
                    i[0] += 1
                    
            a.insert(re[0], [re[0], re[1]])
            print(a, k, '진입')

    for i in a:
        if copy.index(i) == i[0]:
           answer += 'O'
        else:
            answer += 'X'
    return answer

solution(n, k, cmd)