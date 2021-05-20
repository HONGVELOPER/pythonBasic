def bm_mine(str, pat):

    skip = [len(pat)] * 256

    # for pt in range(256):
        # skit[pt] = len(pat)         # skip의 문자들을 patter의 크기로 다 맞춘다.
    for pt in range(len(pat)):
        # skip에서 pat 속에 있는 문자들을  
        print(pat[pt])
        print(ord(pat[pt]), len(pat) - pt - 1)
        skip[ord(pat[pt])] = len(pat) - pt - 1
    
    print(skip)







bm_mine('ABCXDEZCABACABAC', 'ABAC')