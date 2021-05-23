from __future__ import annotations
from typing import Any, Type

class Node:

    def __init__(self, key, value, left, right):
        ''' 생성자(constructor) '''
        self.key = key
        self.value = value
        self.left = left
        self.right = right

class BinarySearchTree:
    
    def __init__(self):

        self.root = None

    def search(self, key):
        p = self.root
        while True:
            if p is None:
                return None
            if key == p.key:
                return p.value
            elif key < p.key:
                return p.left
            else:
                return p.right

    def add(self, key, value):

        def add_node(node, key ,value):
            '''node를 루트로 하는 서브트리에 키가 key이고 값이 value 인 노드를 삽입'''
            if key == node.key:
                return False        # key가 이미 이진 검색 트리에 존재
            elif key < node.key:
                if node.left is None:
                    node.left = Node(key, value, None, None)
                else:
                    add_node(node.left, key, value)         # 재귀 탐색
            else:
                if node.right is None:
                    node.right = Node(key, value, None, None)
                else:
                    add_node(node.right, key, value)
            return True
        if self.root is None:
            self.root = Node(key, value, none, none)
            return True
        else:
            return add_node(self.root, key, value)
    
    def remove(self, key):
        # self.root 가 어디서 선언이 됫나 생각해보니 root 가 없으면 remove 가 안되고,
        # add 함수에서 self.root 선언이 되있다면 root 가 none 일 수 가없다.
        p = self.root           # 스캔 중인 노드
        parent = None           # 스캔 중인 노드의 부모 노드
        is_left_child = True    # p는 parent의 왼쪽 자식인지 확인
        while True:
            if p is None:           # 트리에 KEY 값이 없다.
                return False

            if key == p.key:        # 발견
                break
            else:                   # 찾고 있는 중
                parent = p
                if key < p.key:
                    is_left_child = True
                    p = p.left
                else:
                    is_left_child = False
                    p = p.right

        if p.left is None:              # 왼쪽 자식 노드가 없을 때
            if p is self.root:
                self.root = p.right
            elif is_left_child:
                parent.right = p.right
            else:
                parent.right = p.right
        elif p.right is None:
            if p is self.root:
                self.root = p.left
            elif is_left_child:
                parent.left = p.left
            else:
                parent.right = p.left
        else:
            parent = p
            left = p.left
            is_left_child = True
            while left.right is not None:
                parent = left
                left = left.right
                is_left_child = False
            p.key = left.key
            p.value = left.value
            if is_left_child:
                parent.left = left.left
            else:
                parent.right = left.left

        return True
