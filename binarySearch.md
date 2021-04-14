## 이진 검색
#### 이진 검색은 원소가 오름차순 or 내림차순으로 정렬된 배열에서 좀 더 효율적으로 검색할 수 있는 알고리즘이다.
#### 이진 검색에선 3개의 값을 처음에 설정해야 한다.  left, center, right 이다.
#### left = 0, right = len(sequence)-1, center = (left + right) // 2
#### 이진 검색은 찾고자 하는 값(key 값)이 현재 center값을 index로 갖는 값의 크기와 비교하는 것이다.
#### 현재 center의 값과 key값의 관계에 따라 재정렬을 한다.
#### if (center 값 < key 값) -> left = center+1 로 재정의 한다. -> left 값에 따라 center의 값도 재정의한다.
#### 혹은 if (center 값 > key 값) -> right = center-1 로 재정의 한다. -> right 값에 따라 center의 값도 재정의한다.

#### 이와 같이 절반을 신경 쓰지 않으며 1/2n 과 같은 형태로 변해가며 값을 검색하는 알고리즘이다.
#### 이와 같이 재정의를 하다가 left의 값이 right 의 값보다 커지는 순간 or key 값을 찾은경우 알고리즘은 종료된다.
