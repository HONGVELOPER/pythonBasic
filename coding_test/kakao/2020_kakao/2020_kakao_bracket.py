def solution(p):        # 문자열 p가 올바른 괄호 문자열인지 체크
    balanced = []
    for i in p:
        if i == '(':
            balanced.append(i)
        else:
            balanced.pop()
    return True

def divide(p):      # 문자열 w를 u, v로 분리하는 함수
    count = [0, 0]
    for i in p:
        if i == '(':
            count[0] += 1
        else:
            count[1] += 1



p = "()))((()"
solution(p)