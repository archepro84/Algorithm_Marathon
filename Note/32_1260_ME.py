# graph = {
#     1: [2, 3, 4],
#     2: [4],
#     3: [4],
# }

# graph = {
#     1: [2],
#     3: [1, 4],
#     5: [4, 2]
# }

graph = {
    1: [2],
    2: [5],
    3: [1, 4],
    4: [5],
}

# graph = {
#     1: [2, 3],
#     2: [5],
#     3: [4],
#     4: [5]
# }
# input1, input2 = 3,1
# start_v = 3


# v : 시작하는 정점의 위치
# try catch문으로 마지막 데이터가 존재하는지 확인해야 한다.
def recursive_dfs(v, discovered=[]):
    discovered.append(v)

    if graph.get(v):
        for w in graph[v]:
            # print(w)
            if w not in discovered:
                discovered = recursive_dfs(w, discovered)
    return discovered


# start_v : 시작하는 정점의 위치
def iterative_bfs(start_v):
    discovered = [start_v]
    queue = [start_v]
    while queue:
        v = queue.pop(0)
        if graph.get(v):
            for w in graph[v]:
                if w not in discovered:
                    discovered.append(w)
                    queue.append(w)
    return discovered

result = recursive_dfs(3)
print(result)
result_bfs = iterative_bfs(3)
print(result_bfs)

# print(graph)
# print(graph.get(1))
# print(graph.get(4))
