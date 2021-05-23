class Node:
    ''' 이진 트리 노드 클래스 '''
    def __init__(self, data):
        self.data = data
        self.left_child = None
        self.right_child = None

root_node = Node(2)
node_B = Node(3)
node_C = Node(5)
node_D = Node(7)
node_E = Node(11)

root_node.left_child = node_B
root_node.right_child = node_C

node_B.left_child = node_D
node_B.right_child = node_E

test_node_1 = root_node.left_child
test_node_2 = test_node_1.right_child
# print(test_node_1.data)
# print(test_node_2.data)


# 완전 이진 트리(complete binary tree)
complete_binary_tree = [None, 1, 5, 12, 11, 9, 10, 14, 2, 10]

# pre-order 순회  
# parameter node -> left child node of parameter -> right child node of parameter
def pre_order(node, level):
    level += 1
    print(node.data,  '|', level)
    if node.left_child:
        pre_order(node.left_child, level)
    if node.right_child:
        pre_order(node.right_child, level)

# pre_order(root_node, 0)

# post-order 순회 
# left child node of parameter -> right child node of parameter ->  parameter node
# 왼쪽 부분 트리 순회, 오른쪽 부분 트리 순회, 현재 노드 데이터 출력
def post_order(node):
    if node.left_child:
        post_order(node.left_child)
    if node.right_child:
        post_order(node.right_child)
    print(node.data)

# post_order(root_node)


# in-order 순회
# left child of parameter -> parameter node -> right child of parameter
# 왼쪽 부분 트리 순회, 현재 노드 데이터 출력, 오른쪽 부분 트리 순회
def in_order(node):
    if node.left_child:
        in_order(node.left_child)
    print(node.data)
    if node.right_child:
        in_order(node.right_child)

in_order(root_node)
