from collections import deque
import sys

sys.setrecursionlimit(10005)


class Node:
    def __init__(self, x, y, id, idx):
        self.id = id  # 노드 번호
        self.x = x
        self.y = y

        # node_list 정렬 후 인덱스
        self.idx = idx
        self.left = None
        self.right = None
        self.parent = None


node_list = []


def insert_node(idx):
    par_node = node_list[0]  # root
    cur_node = node_list[idx]
    while True:
        if par_node.x > cur_node.x:
            if par_node.left:
                par_node = node_list[par_node.left]
            else:
                par_node.left = idx
                cur_node.parent = par_node.idx
                break
        elif par_node.x < cur_node.x:
            if par_node.right:
                par_node = node_list[par_node.right]
            else:
                par_node.right = idx
                cur_node.parent = par_node.idx
                break


pre_result = []
post_result = []


def dfs(idx):
    node = node_list[idx]
    pre_result.append(node.id)
    if node.left:
        dfs(node.left)
    if node.right:
        dfs(node.right)
    post_result.append(node.id)


def solution(nodeinfo):
    for i, (x, y) in enumerate(nodeinfo):
        node = Node(x, y, i + 1, -1)
        node_list.append(node)

    node_list.sort(key=lambda node: (-node.y, node.x))

    for idx, node in enumerate(node_list):
        node.idx = idx
        if idx > 0:
            insert_node(idx)

    dfs(0)
    answer = [pre_result, post_result]
    return answer
