def preorder(arr_y, arr_x, answer):
    node = arr_y[0]
    idx = arr_x.index(node)
    arr_y1 = []
    arr_y2 = []
    
    for i in range(1, len(arr_y)):
        if node[0] > arr_y[i][0]:
            arr_y1.append(arr_y[i])
        else:
            arr_y2.append(arr_y[i])
    
    answer.append(node[2])
    if len(arr_y1) > 0:
        preorder(arr_y1, arr_x[:idx], answer)
    if len(arr_y2) > 0:
        preorder(arr_y2, arr_x[idx + 1:], answer)

def postorder(arr_y, arr_x, answer):
    node = arr_y[0]
    idx = arr_x.index(node)
    arr_y1 = []
    arr_y2 = []
    
    for i in range(1, len(arr_y)):
        if node[0] > arr_y[i][0]:
            arr_y1.append(arr_y[i])
        else:
            arr_y2.append(arr_y[i])
    
    if len(arr_y1) > 0:
        postorder(arr_y1, arr_x[:idx], answer)
    if len(arr_y2) > 0:
        postorder(arr_y2, arr_x[idx + 1:], answer)
    answer.append(node[2])


def solution(nodeinfo):
    preanswer = []
    postanswer = []
    
    for i in range(len(nodeinfo)):
        nodeinfo[i].append(i+1)
    
    arr_y = sorted(nodeinfo, key = lambda x : (-x[1], x[0]))
    arr_x = sorted(nodeinfo)
    
    preorder(arr_y, arr_x, preanswer)
    postorder(arr_y, arr_x, postanswer)
    
    return [preanswer, postanswer]

print(solution([[5,3],[11,5],[13,3],[3,5],[6,1],[1,3],[8,6],[7,2],[2,2]]))