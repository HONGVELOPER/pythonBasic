'''
HASH TALBE
1. 고정된 크기의 배열(해쉬 테이블)을 만든다.
2. 해쉬 함수를 이용해서 KEY 를 원하는 범위의 자연수로 바꾼다.
3. 해쉬 함수 결과 값을 INDEX 로 하여 (KEY, VALUE) 쌍을 배열에 집어 넣는다.


HASH FUNCTION
-> 나누기 방법
1. 자연수 KEY를 해쉬 테이블의 크기로 나눈 나머지를 RETURN 한다.

-> 곱하기 방법
1. X 를 임의로 정한다. 여기서 X 는 (0 < X < 1) 사이의 임의의 값이다.
2. KEY * X = Y 라고 할때, Y는 xx.xxxxx 와 같은 소수점이 무조건 있는 형태를 갖는다.
3. Y 에서 정수 부분을 버린 o.xxxxx 부분만 남긴다.
4. 소수부분인 o.xxxxx 에 해쉬 테이블의 크기를 곱한다.
5. 곱한 결과 값의 소수점 부분을 버린다.
ea ) key = 200 / x = 0.6666 / 해쉬 테이블의 크기 = 30 이라 하면
    200 * 0.666 = 133.32 -> y = 0.32
    0.32 * 30 = 9.6 -> final = 9
'''

class Node:

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None

class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def find_node_with_key(self, key):
        ''' 링크드 리스트에서 주어진 데이터를 갖고있는 노드로 리턴한다. 단 해당 노드가 없으면 None 을 return '''
        iterator = self.head

        while iterator is not None:
            if iterator.key == key:
                return iterator
            iterator = iterator.next

        return None

    def appoend(self, key, value):
        # 링크드 리스트 추가 연산 메소드
        new_node = Node(key, value)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node # tail의 다음 노드로 추가
            new_node.prev = self.tail
            self.tail = new_node # tail 업데이트

    def delete(self, node_to_delete):
        
        # 링크드 리스트에서 마지막 남은 데이터를 삭제할 때
        if node_to_delete is self.head and node_to_delete is self.tail:
            self.head = None
            self.tail = None

        # 링크드 리스트 맨 앞 데이터를 삭제할 때
        elif node_to_delete is self.head:
            self.head = self.head.next
            self.head.prev = None

        # 링크드 리스트 맨 뒤 데이터를 삭제할 때
        elif node_to_delete is self.tail:
            self.tail = self.head.prev
            self.tail.next = None
        
        # 링크드 리스트 중간 데이터를 삭제할 때
        else:
            node_to_delete.prev.next = node_to_delete.next
            node_to_delete.next.prev = node_to_delete.prev

    def __str__(self):
        res_str = ''
        iterator = self.head

        while iterator is not None:
            res_str += f'{iterator.key}: {iterator.value} \n'
        iterator = iterator.next
        return res_str