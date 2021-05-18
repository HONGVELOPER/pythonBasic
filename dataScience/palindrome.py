word = 'racecar'


def is_palindrome(word):
    for i in range(len(word) // 2):
        if word[i] != word[-i - 1]:
            return False
    return True


is_palindrome(word)