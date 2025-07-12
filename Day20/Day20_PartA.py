import heapq
from collections import defaultdict

DIRECTIONS = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def neighbors(graph, node, wall_cheats=None, reverse=False):
    max_row = len(graph) - 1
    max_col = len(graph[0]) - 1

    row, col = node

    for dr, dc in DIRECTIONS:
        if reverse: 
            nr, nc = row - dr, col - dc 
        else:
            nr, nc = row + dr, col + dc

        if not (0 <= nr <= max_row and 0 <= nc <= max_col):
            continue

        new_node = (nr, nc)

        can_cheat = False
        if wall_cheats:
            if reverse:
                 for cheat_from, cheat_to in wall_cheats.items():
                    if cheat_to == node and cheat_from == new_node:
                        can_cheat = True
                        break
            else:
                can_cheat = wall_cheats.get(node) == new_node

        is_wall = graph[nr][nc] == '#'
        
        if not is_wall or can_cheat:
            yield new_node

def dijkstra_all_distances(maze, start_node, walls_cheats=None, reverse=False):
    all_distances = {start_node: 0}
    priority_queue = [(0, start_node)]

    while priority_queue:
        distance_to_node, node = heapq.heappop(priority_queue)

        if distance_to_node > all_distances.get(node, float('inf')):
            continue

        for to_neighbor in neighbors(maze, node, walls_cheats, reverse):
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
distances_to_end = dijkstra_all_distances(graph, end, reverse=True)

initial_min_time = distances_from_start.get(end)

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

for p_row in range(rows):
    for p_col in range(cols):
        node = (p_row, p_col)

        # We only care about starting cheats from open cells
        if graph[p_row][p_col] == '#':
            continue

        for dr1, dc1, dr2, dc2 in WALL_CHEAT_OFFSETS:
            first_wall_pos = (p_row + dr1, p_col + dc1)
            second_open_pos = (p_row + dr2, p_col + dc2)

            fw_row, fw_col = first_wall_pos
            sw_row, sw_col = second_open_pos

            is_in_bounds = all([
                0 <= fw_row < rows,
                0 <= fw_col < cols,
                0 <= sw_row < rows,
                0 <= sw_col < cols
            ])

            if not is_in_bounds:
                continue

            is_first_wall_actual_wall = graph[fw_row][fw_col] == '#'
            is_second_wall_not_wall = graph[sw_row][sw_col] != '#'

            if not (is_first_wall_actual_wall and is_second_wall_not_wall):
                continue

            cheat_from_node = node
            cheat_to_node = second_open_pos

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

            if cheat_time < initial_min_time:
                saved_time = initial_min_time - cheat_time
                cheats_per_saved_time[saved_time] += 1

print("\nDistances per cheat:")
total_cheats_100 = 0
for saved_time, total_cheats in sorted(cheats_per_saved_time.items()):
    if saved_time >= 100:
        total_cheats_100 += total_cheats
    print(f"There {'are' if total_cheats > 1 else 'is'} {total_cheats} cheats that save {saved_time} picoseconds.") 

print(f"Total cheats that save more than 100 picoseconds: {total_cheats_100}")
