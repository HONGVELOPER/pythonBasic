class Node:

    def __init__(self, data):
        self.data = data
        self.parent = None
        self.left_child = None
        self.right_child = None

def print_inorder(node):
    if node is not None:
        print_inorder(node.left_child)
        print(node.data)
        print_inorder(node.right_child)

class BinarySearchTree:

    def __init__(self):
        self.root = None

    def print_sorted_tree(self):
        ''' 이진 탐색 트리 내의 데이터를 정렬된 순서로 출력해주는 메소드 '''
        print_inorder(self.root)
        

bst = BinarySearchTree()

