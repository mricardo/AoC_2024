
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
        
def dijsktra(graph, maze, start, goal):
    frontier = [(0, start)]
    came_from = {}
    cost_so_far = {}

    came_from[start] = None
    cost_so_far[start] = 0

    while frontier:
        current = heapq.heappop(frontier)[1]

        if current[0] == goal:
            return came_from, cost_so_far[current], current

        update_graph(graph, maze, current)

        for next in graph.get(current, []):
            new_cost = cost_so_far[current] + graph[current][next]
            if next not in cost_so_far or new_cost < cost_so_far[next]:
                cost_so_far[next] = new_cost
                
                
                came_from[next] = {current}

                heapq.heappush(frontier, (new_cost, next))
            elif new_cost == cost_so_far[next]:
                came_from[next].add(current)

    return None, float('inf')  # No path found

def walk_backwards(min_paths, start_coord, end_coord):
    path = [end_coord[0]]

    new_predessors = []

    predecessors = min_paths[end_coord]
 
    while len(predecessors) > 0:
        for p in predecessors:
            if p[0] not in path:
                path.insert(0, p[0])          

            if min_paths[p]:
                new_predessors.extend(min_paths[p])
        
        predecessors = new_predessors[:]
        new_predessors = []
        
    return path
    
if __name__ == "__main__":
    filename = "Day16_test.txt"

    maze = []
    with open(filename, 'r') as f:
        lines = f.readlines()

        i = 0
        start_coord = (-1,-1)
        end_coord = (-1,-1)
        while i < len(lines):
            row = list(lines[i].strip())
            maze.append(row)

            if "S" in row:
                j = row.index("S")
                start_coord = (i, j)
            
            if "E" in row:
                j = row.index("E")
                end_coord = (i, j)
            
            i += 1
      
    min_paths, min_cost, end_coord = dijsktra({}, maze, (start_coord, "E"), end_coord)
  
    path = walk_backwards(min_paths, start_coord, end_coord)
    print("Visited Nodes: ", len(path))