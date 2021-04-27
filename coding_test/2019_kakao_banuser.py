user_id = ["frodo", "fradi", "crodo", "abc123", "frodoc"]
banned_id = ["fr*d*", "abc1**"]

def solution(user_id, banned_id):
    answer = 0
    for i in user_id:
        for j in i:
            print(j)
    return answer




solution(user_id, banned_id)