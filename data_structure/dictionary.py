# dictionary 특징 : 1개의 key에 1개의 value 를 갖어야 한다.
# dictionary 선언
grades = {}

# key - vale 데이터 삽입
grades['현승'] = 80
grades['태호'] = 60
grades['영훈'] = 90
grades['지웅'] = 70
grades['동욱'] = 96

print(grades)

# key 로 접근하여 데이터 수정 가능 (list 와 비슷)
grades['현승'] = 100

print(grades)

# key 를 이용한 value 탐색
print(grades['동욱'])
print(grades['현승'])

# key 를 이용한 value 삭제
grades.pop('태호')
grades.pop('지웅')

print(grades)