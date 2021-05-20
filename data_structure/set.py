# dictionary 와 비슷해 보이지만, key-value 쌍이 아니며, 
# 데이터 간의 중복을 허용하지 않는다는 특징이 있다.
# 또한, 데이터 간의 순서를 보장 하지 않는다.

finished_classes = set()

# 데이터 저장
finished_classes.add('자료 구조')
finished_classes.add('알고리즘')
finished_classes.add('프로그래밍 기초')
finished_classes.add('인터렉티브 웹')
finished_classes.add('데이터 사이언스')

print(finished_classes)

# 중복 데이터 저장 시도
finished_classes.add('데이터 사이언스')
# 오류는 나지 않지만, 데이터가  추가 되거나 하지는 않는다.

# 데이터 탐색
print('컴퓨터 개론' in finished_classes)        # False
print('자료 구조' in finished_classes)          # True

# 데이터 삭제
finished_classes.remove('자료 구조')
finished_classes.remove('알고리즘')

print(finished_classes)