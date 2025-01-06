import heapq

def update_maze(maze, path, start, goal):
    for p in path:
        i,j = p[0][0], p[0][1]
        if (i,j) == start or (i,j) == goal:
            continue

        direction = p[1]

        if direction == "E":
            maze[i][j] = '>'
        if direction == "N":
            maze[i][j] = '^'
        if direction == "S":
            maze[i][j] = 'v'
        if direction== "W":
            maze[i][j] = '<'

def print_maze(maze):    
    for r in maze:
        print(*r, sep= " ")
    
def heuristic(a, b):
    """Manhattan distance heuristic."""
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def update_graph(graph, maze, current):
    if current not in graph:
        graph[current] = {}
    
    i, j = current[0]
    direction = current[1]

    if direction == "E" and maze[i][j+1] != '#':
        graph[current][((i, j+1), "E")] = 1                
    if direction == "W" and maze[i][j-1] != "#":
        graph[current][((i, j-1), "W")] = 1
    if direction == "S" and maze[i+1][j] != "#":
        graph[current][((i+1, j), "S")] = 1
    if direction == "N" and maze[i-1][j] != "#":
        graph[current][((i-1, j), "N")] = 1
    
    for d in ["N", "W", "S", "E"]:
        if d != direction:
            graph[current][((i, j), d)] = 1000
        
def a_star_search(graph, maze, start, goal):
    frontier = [(0, start)]
    came_from = {}
    cost_so_far = {}

    came_from[start] = None
    cost_so_far[start] = 0

    while frontier:
        current = heapq.heappop(frontier)[1]

        if current[0] == goal:
            last_goal = current
            path = []
            while current:
                path.insert(0, current)
                current = came_from[current]
        
            return path, cost_so_far[last_goal]

        update_graph(graph, maze, current)

        for next in graph.get(current, []):
            new_cost = cost_so_far[current] + graph[current][next]
            if next not in cost_so_far or new_cost < cost_so_far[next]:
                cost_so_far[next] = new_cost
                priority = new_cost + heuristic(next[0], goal)
                heapq.heappush(frontier, (priority, next))
                came_from[next] = current

    return None, float('inf')  # No path found

if __name__ == "__main__":
    filename = "Day16_test.txt"

    maze = []
    with open(filename, 'r') as f:
        lines = f.readlines()

        i = 0
        s_coord = (-1,-1)
        e_coord = (-1,-1)
        while i < len(lines):
            row = list(lines[i].strip())
            maze.append(row)

            if "S" in row:
                j = row.index("S")
                s_coord = (i, j)
            
            if "E" in row:
                j = row.index("E")
                e_coord = (i, j)
            
            i += 1

    
    print("S Coord: ", s_coord)
    print("E Coord: ", e_coord)
    
    path, cost = a_star_search({}, maze, (s_coord, "E"), e_coord)
    update_maze(maze, path, s_coord, e_coord)
    print_maze(maze)
    
    print("Cost: ", cost)