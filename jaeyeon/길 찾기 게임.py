import sys

# 재귀한도 늘려주기
sys.setrecursionlimit(10**6)


class Node:
    def __init__(self, x, y, head):
        self.x = x
        self.y = y
        self.head = head
        self.left_child = None
        self.right_child = None


class Tree:
    def __init__(self, x, y, head):
        self.root = Node(x, y, head)

    def append_node(self, x, y, head):
        cur_node = self.root
        # 빈 공간 찾기
        while True:
            if x < cur_node.x:
                if cur_node.left_child:
                    cur_node = cur_node.left_child
                else:
                    cur_node.left_child = Node(x, y, head)
                    break
            else:
                if cur_node.right_child:
                    cur_node = cur_node.right_child
                else:
                    cur_node.right_child = Node(x, y, head)
                    break


pre = []
post = []


# 재귀로 head -> left -> right 순서로 순회
def preorder(cur_node):
    if cur_node:
        pre.append(cur_node.head)
        if cur_node.left_child:
            preorder(cur_node.left_child)
        if cur_node.right_child:
            preorder(cur_node.right_child)


# 재귀로 left -> right -> head 순서로 순회
def postorder(cur_node):
    if cur_node:
        if cur_node.left_child:
            postorder(cur_node.left_child)
        if cur_node.right_child:
            postorder(cur_node.right_child)
        post.append(cur_node.head)


def solution(nodeinfo):
    # 노드 번호 붙여주기
    for idx, node in enumerate(nodeinfo):
        nodeinfo[idx] = node + [idx + 1]
    nodeinfo.sort(key=lambda x: -x[1])

    # 트리 만들기
    tree = Tree(*nodeinfo[0])
    for idx, node in enumerate(nodeinfo):
        if idx == 0:
            continue
        tree.append_node(*node)

    # 순회
    preorder(tree.root)
    postorder(tree.root)

    return [pre, post]
