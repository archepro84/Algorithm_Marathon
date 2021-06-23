import collections
import sys

n, m, v = map(int, sys.stdin.readline().split())
# 0,0 인덱스는 사용하지 않기 때문에 range(n + 1)을 해 리스트를 1 올린다.
matrix = [[0] * (n + 1) for i in range(n + 1)]

for i in range(m):
    a, b = map(int, sys.stdin.readline().split(' '))
    # 좌우 대칭으로 만들어 양방향 통행이 가능하도록 설정
    matrix[a][b] = 1
    matrix[b][a] = 1


# 방문했던 index의 위치를 저장하기 위한 리스트
visit_list = [0] * (n + 1)

result_dfs = []
result_bfs = []


def dfs(v):
    # 현재 vertex의 위치를 추가하여 방문 기록을 남긴다.
    visit_list[v] = 1
    # 방문 했던 위치 순서대로 결과값에 삽입한다.
    result_dfs.append(v)

    # 총 정점의 갯수만큼 for문을 실행한다.
    for i in range(1, n + 1):
        # 방문을 하지 않았으며, 이동할 수 있는 간선이 존재할 경우
        if (visit_list[i] == 0 and matrix[v][i] == 1):
            dfs(i)


def bfs(v):
    # 방문할 수 있는 인덱스의 위치를 큐의 형태로 저장한다.
    queue = collections.deque([v])
    # 방문한 위치를 0으로 변경한다.
    visit_list[v] = 0

    while queue:
        # q에 먼저 입력된 데이터를 출력한다.
        v = queue.popleft()
        # 방문한 bfs의 순서대로 결과값을 지정한다.
        result_bfs.append(v)
        # 총 정점의 갯수만큼 for문을 실행
        for i in range(1, n + 1):
            # DFS에서 방문을 했으며, 이동가능한 간선이 존재할 경우
            if (visit_list[i] == 1 and matrix[v][i] == 1):
                # 이동 가능한 간선을 queue에 추가한다.
                queue.append(i)
                # 방문했던 리스트의 위치를 0으로 변경한다.
                visit_list[i] = 0


dfs(v)
bfs(v)

for x in result_dfs:
    print(x, end=" ")
print()
for x in result_bfs:
    print(x, end=" ")
