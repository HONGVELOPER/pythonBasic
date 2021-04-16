from typing import Any, Sequence

def bin_search(a: Sequence, key: Any) -> int:
  pl = 0
  pr = len(a) - 1

  while True:
    # pc의 값은 딱 맞아 떨어지지 않을경우 왼쪽값으로 정의한다.
    pc = (pl + pr) // 2 
    if a[pc] == key:
      return pc

    # 찾고자 하는 값이 pc보다 커서, pl을 pc + 1 로 재정의한다.
    elif a[pc] < key:
      pl = pc + 1
    
    # 찾고자 하는 값이 pc 보다 작아, pr을 pc - 1 로 재정의한다.
    else:
      pr = pc - 1
    # pl 값이 pr 보다 커진 경우에는 찾고자 하는 값이 존재하지 않기에 -1 을 return 시킨다.
    if pl > pr:
      break    
    return -1

if __name__ == '__main__':
  num = int(input('원소 수를 입력해주세요. :'))
  x = [None] * num

  print('배열 데이터를 오름차순으로 입력하세요.')

  x[0] = int(input('x[0]: '))

  for i in range(1, num):
    while True:
      x[i] = int(input(f'x[{i}]: '))
      if x[i] >= x[i - 1]:
        break

  ky = int(input('검색할 값을 입력해주세요. :'))
  idx = bin_search(x, ky)

  if idx == -1:
    print('검색값을 갖는 원소가 존재하지 않습니다.')
  else:
    print(f'검색값은 x[{idx}]에 있습니다.')