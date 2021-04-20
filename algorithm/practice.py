del_list = []
def solution(new_id):
    new_id = new_id.lower()
    new_id = list(new_id)
    answer = special_delete(new_id)
    return answer
def special_delete(new_id):
    for i, value in enumerate(new_id):
        if not (value.isalpha() or value.isdigit() or value == '-' or value == '_' or value == '.'):
            del_list.append(i)
        elif value == '.':
            if i + 1 <= len(new_id) - 1:
                if new_id[i + 1] == '.':
                    del_list.append(i+1)
            elif new_id[0] == '.':
                del_list.append(0)
            elif i == len(new_id) - 1:
                del_list.append(i)
    if len(new_id) <= 2:
        if len(new_id) == 0:
            new_id = 'a'
        while len(new_id) == 3:
            new_id + new_id[len(new_id)-1]
    elif len(new_id) >= 16:
        num = len(new_id)
        i = 16
        while num == 15:
            del_list.append(i)
            i += 1
            num -= 1
    del_set = set(del_list)
    num = 0
    for i in del_set:
        del new_id[i-num]
        num += 1
    return new_id