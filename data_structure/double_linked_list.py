class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, data):
        ''' 링크드 리스트 추가 연산 메소드 '''
        new_node = Node(data)

        # 링크드 리스트가 비어 있는 경우
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else: # 링크드 리스트에 데이터가 있는 경우
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
    
    def prepend(self, data):
        """링크드 리스트 가장 앞에 데이터를 추가시켜주는 메소드"""
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.head.prev = new_node
            new_node.next = self.head
            self.head =  new_node

    def insert_after(self, previous_node, data):
        new_node = Node(data)
        if self.tail is previous_node:
            self.append(data)
        else:
            new_node.prev = previous_node
            new_node.next = previous_node.next
            previous_node.next.prev = new_node
            previous_node.next = new_node

    def delete(self, node_to_delete):
        if self.head is self.tail:
            self.head = None
            self.tail = None
        elif self.head is node_to_delete:
            self.head = self.head.next
            self.head.prev = None
        elif self.tail is node_to_delete:
            self.tail = self.tail.prev
            self.tail.next = None
        else:
            node_to_delete.prev.next = node_to_delete.next
            node_to_delete.next.prev = node_to_delete.prev

    def find_node_at(self, index):
        """링크드 리스트 접근 연산 메소드. 파라미터 인덱스는 항상 있다고 가정한다"""
        
        iterator = self.head  # 링크드 리스트를 돌기 위해 필요한 노드 변수
        
        # index 번째 있는 노드로 간다
        for _ in range(index):
            iterator = iterator.next
        
        return iterator

    def find_node_with_data(self, data):
        """링크드 리스트에서 주어진 데이터를 갖고있는 노드를 리턴한다. 단, 해당 노드가 없으면 None을 리턴한다"""
        iterator = self.head  # 링크드 리스트를 돌기 위해 필요한 노드 변수
        
        while iterator is not None:
            if iterator.data == data:
                return iterator

            iterator = iterator.next

        return None

    def __str__(self):
        """링크드 리스트를 문자열로 표현해서 리턴하는 메소드"""
        res_str = "|"

        # 링크드 리스트 안에 모든 노드를 돌기 위한 변수. 일단 가장 앞 노드로 정의한다.
        iterator = self.head

        # 링크드 리스트 끝까지 돈다
        while iterator is not None:
            # 각 노드의 데이터를 리턴하는 문자열에 더해준다
            res_str += " {} |".format(iterator.data)
            iterator = iterator.next  # 다음 노드로 넘어간다

        return res_str


my_list = LinkedList()

my_list.append(2)
my_list.append(3)
my_list.append(5)
my_list.append(7)
a = my_list.find_node_at(3)

print(my_list)


