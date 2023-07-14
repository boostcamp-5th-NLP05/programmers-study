# 미통과 풀이
pre_result = []
post_result = []


def pre(nodeinfo):
    print("pre")
    nodeinfo.sort(key=lambda x: (-x[1]))
    pre_result.append(nodeinfo[0])
    nodeinfo.sort(key=lambda x: (x[0]))
    left = nodeinfo[:len(nodeinfo) // 2]
    right = nodeinfo[len(nodeinfo) // 2:]
    pre(left)
    pre(right)


def post(nodeinfo):
    print("pre")
    nodeinfo.sort(key=lambda x: (-x[1]))

    nodeinfo.sort(key=lambda x: (x[0]))
    left = nodeinfo[:len(nodeinfo) // 2]
    right = nodeinfo[len(nodeinfo) // 2:]
    post(right)
    post(left)
    pre_result.append(nodeinfo[0])


def solution(nodeinfo):
    answer = []
    nodeinfo.sort()
    pre(nodeinfo)
    post(nodeinfo)

    answer.append(pre_result)
    answer.append(post_result)

    return answer