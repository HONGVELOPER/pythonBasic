# 내 생각대로 구현해본것
def bf_mine(pat, string):
    pat_idx = 0
    str_idx = 0
    now_str_idx = 0
    pat_length = len(pat)
    while pat_idx != pat_length:
        if string[str_idx] == pat[pat_idx]:
            pat_idx += 1
            str_idx += 1
        else:
            pat_idx = 0
            now_str_idx += 1
            str_idx = now_str_idx
    print(f'찾고자 하는 값이 {now_str_idx} 번째 index 부터 시작합니다.')

# 브루트 포스법으로 문자열 검색하기
def bf_match(txt: str, pat: str) -> int:
    pt = 0      # txt 를 따라가는 커서
    pp = 0      # pat 를 따라가는 커서
    
    while pt != len(txt) and pp != len(pat):
        if txt[pp] == pat[pp]:
            pt += 1
            pp += 1
        else:
            pt = pt - pp + 1
            pp = 0
    return pt - pp if pp == len(pat) else -1
