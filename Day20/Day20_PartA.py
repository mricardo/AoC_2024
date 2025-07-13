import heapq
from collections import defaultdict

DIRECTIONS = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def neighbors(graph, node):
    max_row = len(graph) - 1
    max_col = len(graph[0]) - 1

    row, col = node

    for dr, dc in DIRECTIONS:
        nr, nc = row + dr, col + dc

        if not (0 <= nr <= max_row and 0 <= nc <= max_col):
            continue

        new_node = (nr, nc)

        is_wall = graph[nr][nc] == '#'
        
        if not is_wall:
            yield new_node

def dijkstra_all_distances(maze, start_node):
    all_distances = {start_node: 0}
    priority_queue = [(0, start_node)]

    while priority_queue:
        distance_to_node, node = heapq.heappop(priority_queue)

        if distance_to_node > all_distances.get(node, float('inf')):
            continue

        for to_neighbor in neighbors(maze, node):
            new_distance = distance_to_node + 1

            if new_distance < all_distances.get(to_neighbor, float('inf')):
                all_distances[to_neighbor] = new_distance
                heapq.heappush(priority_queue, (new_distance, to_neighbor))

    return all_distances

# Day 20 - Part A
graph = []
start = end = (-1, -1)

with open("Day20/Day20_Input.txt", "r") as file:
    for r_idx, line in enumerate(file): # Use enumerate for row index
        stripped_line = line.strip()
        graph.append(list(stripped_line))

        if 'S' in stripped_line:
            start = (r_idx, stripped_line.index('S'))
        if 'E' in stripped_line:
            end = (r_idx, stripped_line.index('E'))

distances_from_start = dijkstra_all_distances(graph, start)
distances_to_end = dijkstra_all_distances(graph, end)

initial_time = distances_from_start.get(end)

cheats_per_saved_time = defaultdict(int)
processed_cheats = set()

# (row1, col1, row2, col2)
WALL_CHEAT_OFFSETS = [
    (0, 1, 0, 2),   # Right (from node (r,c) to (r, c+2) over wall at (r, c+1))
    (0, -1, 0, -2), # Left
    (1, 0, 2, 0),   # Down
    (-1, 0, -2, 0)  # Up
]

rows = len(graph)
cols = len(graph[0])

for r in range(rows):
    for c in range(cols):
        node = (r, c)

        # We only care about starting cheats from open cells
        if graph[r][c] == '#':
            continue

        for r1, c1, r2, c2 in WALL_CHEAT_OFFSETS:
            wall = (r + r1, c + c1)
            open_position = (r + r2, c + c2)

            wall_row, wall_col = wall
            open_row, open_col = open_position

            is_in_bounds = all([
                0 <= wall_row < rows,
                0 <= wall_col < cols,
                0 <= open_row < rows,
                0 <= open_col < cols
            ])

            if not is_in_bounds:
                continue

            is_wall = graph[wall_row][wall_col] == '#'
            is_open_position = graph[open_row][open_col] != '#'

            if not (is_wall and is_open_position):
                continue

            cheat_from_node = node
            cheat_to_node = open_position

            cheat_key = (cheat_from_node, cheat_to_node)
            if cheat_key in processed_cheats:
                continue

            processed_cheats.add(cheat_key)

            start_to_cheat = distances_from_start.get(cheat_from_node, float('inf'))
            end_to_cheat = distances_to_end.get(cheat_to_node, float('inf'))

            # if there is a wall cheat that does not connect start and end, skip it
            if start_to_cheat == float('inf') or end_to_cheat == float('inf'):
                continue

            cheat_time = start_to_cheat + 1 + end_to_cheat

            if cheat_time < initial_time:
                saved_time = initial_time - cheat_time
                cheats_per_saved_time[saved_time] += 1

print("\nDistances per cheat:")
total_cheats_50 = 0
for saved_time, total_cheats in sorted(cheats_per_saved_time.items()):
    if saved_time >= 100:
        total_cheats_50 += total_cheats
  
print(f"Total cheats that save more than 50 picoseconds: {total_cheats_50}")
