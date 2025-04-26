import sys
from collections import deque

def get_neighbors(node, max_coord, obstacles):
    x, y = node
    possible_neighbors = [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]
    for new_x, new_y in possible_neighbors:
        if 0 <= new_x <= max_coord and 0 <= new_y <= max_coord and (new_x, new_y) not in obstacles:
            yield (new_x, new_y)

def bfs(obstacles, start_node, max_coord):
    distances = {start_node: 0}
    queue = deque([start_node])

    while queue:
        current_node = queue.popleft()
        current_distance = distances[current_node]

        for neighbor in get_neighbors(current_node, max_coord, obstacles):
            if neighbor not in distances:
                distances[neighbor] = current_distance + 1
                queue.append(neighbor)
    return distances

corrupted_coordinates = [tuple(map(int, line.strip().split(','))) for line in sys.stdin]
max_coord = 70
bytes_simulation = 1024
start_node = (0, 0)

maze = [['.' for _ in range(max_coord + 1)] for _ in range(max_coord + 1)]

obstacles = set(corrupted_coordinates)
for r, c in obstacles:
    if 0 <= r <= max_coord and 0 <= c <= max_coord:
        maze[c][r] = '#'

distances = bfs(set(corrupted_coordinates[:bytes_simulation]), start_node, max_coord)

for r in range(max_coord + 1):
    for c in range(max_coord + 1):
        if (c, r) in distances:
            maze[r][c] = 'O'

for row in maze:
    print(''.join(row))

if (max_coord, max_coord) in distances:
    print(distances[(max_coord, max_coord)])
else:
    print("Destination not reachable")