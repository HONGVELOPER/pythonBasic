# 보이어 무어법으로 문자열 검색하기 (문자열 길이는 0~255개)

def bm_match(txt: str, pat: str) -> int:

    skip = [None] * 256
    
    for pt in range(256):
        skip[pt] = len(pat)

    for pt in range(len(pat)):
        skip[ord(pat[pt])] = len(pat) - pt - 1

    # 문자열 검색
    print(pt, 'pt')
    while pt < len(txt):
        print(pt)
        pp = len(pat) - 1 # pp는 pattern의 끝 문자를 나타내는 index 이다.
        while txt[pt] == pat[pp]: # txt와 pat의 글자가 같다면 ?
            if pp == 0: # pp가 -1 씩 줄면서 0이 되면 txt에서 pat과 같은 글자를 발견햇다는 뜻이다. !
                return pt
            pt -= 1
            pp -= 1
        
        pt += skip[ord(txt[pt])] if skip[ord(txt[pt])] >    len(pat) - pp else len(pat) - pp

    return -1

if __name__ == '__main__':
    s1 = input('텍스트를 입력해주세요. :')
    s2 = input('패턴을 입력해주세요. :')

    idx = bm_match(s1, s2)

    if idx == -1:
        print('텍스트 안에 패턴이 존재하지 않습니다.')
    else:
        print(f'{(idx + 1)}번째 문자가 일치합니다.')