# s = "aabbaccc"
# s = "ababcdcdababcdcd"
# s = "abcabcabcabcdededededede"
# s = "abcabcdede"
s = "1234567"

def solution(s):
    min_length = 1001
    for i in range(1, len(s) // 2 + 1):         # 문자 간격을 바꾸기 위한 for문
        compress_count = 0
        remember = None
        for j in range(len(s)):                 # 문자 간격만큼 오른쪽으로 움직이기 위한 for문
            left = i * j
            right = left + i
            if s[left:right] == s[right:right+i] and len(s[left:right]) > 0:
                if remember != s[left:right] and s[left:right] == s[right:right+i]:
                    compress_count += len(s[left:right]) - 1
                elif remember == s[left:right] and s[left:right] == s[right:right+i]:
                    compress_count += len(s[left:right])
                print(remember, '!', s[left:right])
                remember = s[left:right]
        print(compress_count, len(s))
        min_length = min(min_length, len(s) - compress_count)
    print(min_length)
    return min_length

solution(s)