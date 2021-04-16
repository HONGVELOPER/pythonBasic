# number = input('방 번호를 입력해주세요. :')

# same_count = []
# six_nine = 0

# for i in range(len(number)):
#   count = 0
#   if number[i] == '6' or number[i] == '9':
#     six_nine += 1

#   else:
#     for j in range(i + 1, len(number)):
#       if number[i] == number[j]:
#         count += 1
#     same_count.append(count + 1)

# print(same_count, 'sameCount')
# print(six_nine, 'sixnine')
  
# if six_nine % 2 == 0:
#   six_nine = six_nine // 2
# else:
#   six_nine = six_nine // 2 + 1

# print(max(six_nine, max(same_count)))

n = input()
number = [0] * 10
sixnine = 0

for i in range(10):
    number[i] = n.count(str(i))
    if i == 6 or i == 9:
        number[i] = 0
        sixnine += n.count(str(i))  
big = max(number)

if sixnine % 2 == 0:
    sixnine = sixnine // 2
else:
    sixnine = sixnine // 2 + 1

answer = max(sixnine, big)
print(answer)