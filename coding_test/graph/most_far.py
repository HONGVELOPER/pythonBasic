# 가장 먼 노드를 찾아라

def solution(n, edge):
    index_array = []
    for i in range(0, n):
        index_array.append({})
    for i in range(len(edge)):
        if edge[i][0] > edge[i][1]:
            edge[i][0], edge[i][1] = edge[i][1], edge[i][0]
        # index_array[edge[i][0]].append(edge[i][1])
        # print(edge[i])
    # print(in)
    print(index_array[0])

n = 6
# edge = [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]
edge = [[1, 3], [1, 2], [2, 3], [2, 4], [2, 5], [3, 4], [3, 6]]

solution(n, edge)
