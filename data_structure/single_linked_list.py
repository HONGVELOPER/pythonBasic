class Node:
    ''' linked list node class '''

    def __init__(self, data):
        self.data = data # 노드가 저장하는 데이터
        self.next = None # 다음 노드에 대한 reference

class LinkedList:
    ''' linked list class '''
    
    def __init__(self):
        self.head = None
        self.tail = None

    def find_node_at(self, index):
        ''' 링크드 리스트 접근 연산 메소드, 파라미터 index 가 있다고 가정 '''
        iterator = self.head

        for _ in range(index):
            iterator = iterator.next

        return iterator
    
    def find_node_with_data(self, value):
        iterator = self.head
        while iterator is not None:
            if iterator.data == value:
                return iterator
        return None


    def append(self, data):
        ''' 링크드 리스트 추가 연산 메소드 '''

        new_node = Node(data)

        if self.head is None: # 링크드 리스트가 비어 있는 경우
            self.head = new_node
            self.tail = new_node
        else: # 링크드 리스트가 비어있지 않은 경우
            self.tail.next = new_node
            self.tail = new_node

    def __str__(self):
        ''' 링크드 리스트를 문자열로 return '''
        res_str = '|'
        # 링크드 리스트 안에 모든 노드를 반복하기 위한 변수, 일단 가장 앞 노드로 정의
        iterator = self.head

        # 링크드 리스트 반복
        while iterator is not None:
            res_str += f' {iterator.data} |'
            iterator = iterator.next

        return res_str

       
    def insert_after(self, previous_node, data):
        ''' 링크드 리스트에 주어진 노드 뒤 삽입 연산 메소드 '''
        insert_node = Node(data)

        if previous_node is self.tail:
            self.tail.next = insert_node
            self.tail = insert_node
        else:
            insert_node.next = previous_node.next
            previous_node.next = insert_node
    
    def delete_after(self, previous_node):
        ''' 링크드 리스트 삭제연산, 주어진 노드 뒤 삭제한다. '''
        del_data = previous_node.next.data
        if previous_node.next is self.tail:
            previous_node.next = None
            self.tail = previous_node
        else:
            previous_node.next = previous_node.next.next
        return del_data

        

# 새로운 링크드 리스트 선언
linked_list = LinkedList()

# 링크드 리스트에 값 추가 [2, 3, 5, 7]
linked_list.append(2)
linked_list.append(3)
linked_list.append(5)
linked_list.append(7)
linked_list.append(11)

# index 가 2 인 node 를 찾아 node_2 에 넣음
node_2 = linked_list.find_node_at(2)

# 링크드 리스트에서 node_2 뒤에 data가 6인 node 삽입
# linked_list.insert_after(node_2, 6)

# 링크드 리스트에서 node_2 뒤에 node 삭제
linked_list.delete_after(node_2)
print(linked_list)

second_to_last_node = linked_list.find_node_at(2)
linked_list.delete_after(second_to_last_node)

print(linked_list)





    
