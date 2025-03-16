from collections import deque


def calculate_position(move, initial_position):
    move_deltas = {
        '^': (-1, 0),
        'v': (1, 0),
        '<': (0, -1),
        '>': (0, 1),
    }

    dx, dy = move_deltas.get(move)

    return (initial_position[0] + dx, initial_position[1] + dy)

# bfs strategy to move boxes
def move_boxes(warehouse, robot_position, move):
    visited = set()  
    queue = deque([robot_position])  
    visited_order = []  
    
    all_boxes_can_move = True

    visited.add(robot_position)
    visited_order.append(robot_position)

    while queue and all_boxes_can_move:
        current_node = queue.popleft()  # Get the next node from the queue
        neighbors =[]

        if move == '<':
            if warehouse[current_node[0]][current_node[1] - 1] == '#':
                all_boxes_can_move = False
                break
        
            if warehouse[current_node[0]][current_node[1] - 1] in ['[', ']']:
                neighbors = [(current_node[0], current_node[1] - 1)]
                        
        if move == '>':             
            if warehouse[current_node[0]][current_node[1] + 1] == '#':
                all_boxes_can_move = False
                break            
        
            if warehouse[current_node[0]][current_node[1] + 1] in ['[', ']']:
                neighbors = [(current_node[0], current_node[1] + 1)]
            
            
        if move == 'v':             
            if warehouse[current_node[0] + 1][current_node[1]] == '#':
                all_boxes_can_move = False
                break

            if warehouse[current_node[0] + 1][current_node[1]] == '[':
                neighbors = [(current_node[0] + 1, current_node[1]), (current_node[0] + 1, current_node[1] + 1)]
            
            if warehouse[current_node[0] + 1][current_node[1]] ==']':
                neighbors = [(current_node[0] + 1, current_node[1] - 1), (current_node[0] + 1, current_node[1])]

        if move == '^':             
            if warehouse[current_node[0] - 1][current_node[1]] == '#':
                all_boxes_can_move = False
                break

            if warehouse[current_node[0] - 1][current_node[1]] == '[':
                neighbors = [(current_node[0] - 1, current_node[1]), (current_node[0] - 1, current_node[1] + 1)]
            
            if warehouse[current_node[0] - 1][current_node[1]] ==']':
                neighbors = [(current_node[0] - 1, current_node[1] - 1), (current_node[0] - 1, current_node[1])]

        for neighbor in neighbors:
            if neighbor not in visited:
                visited.add(neighbor)
                visited_order.append(neighbor)
                queue.append(neighbor)
    
    #print("Can move: ", all_boxes_can_move, "Visited Order: ", visited_order)

    if all_boxes_can_move:        
        if move == '<':
            robot_position = (robot_position[0], robot_position[1] - 1)

            visited_order.sort(key=lambda item: item[1])
        
            for v in visited_order:
                warehouse[v[0]][v[1] - 1] = warehouse[v[0]][v[1]]
                warehouse[v[0]][v[1]] = '.'
               
        if move == '>': 
            robot_position = (robot_position[0], robot_position[1] + 1)

            visited_order.sort(key=lambda item: item[1], reverse=True)
        
            for v in visited_order:
                warehouse[v[0]][v[1] + 1] = warehouse[v[0]][v[1]]
                warehouse[v[0]][v[1]] = '.'
               
    
        if move == '^': 
            robot_position = (robot_position[0] - 1, robot_position[1])

            visited_order.sort(key=lambda item: item[0])
        
            for v in visited_order:
                warehouse[v[0] - 1][v[1]] = warehouse[v[0]][v[1]]
                warehouse[v[0]][v[1]] = '.'   
         
        if move == 'v': 
            robot_position = (robot_position[0] + 1, robot_position[1])

            visited_order.sort(key=lambda item: item[0], reverse=True)
      
            for v in visited_order:
                warehouse[v[0] + 1][v[1]] = warehouse[v[0]][v[1]]
                warehouse[v[0]][v[1]] = '.'

        
    return robot_position

def run_move(warehouse, move, current_position):    
    current_position = move_boxes(warehouse, current_position, move)
    #print("New Position: ", current_position)

    return current_position

def run_moves(warehouse, moves, current_positions):
    for move in moves:                
        current_positions = run_move(warehouse, move, current_positions)

def print_warehouse(title, warehouse):
    print(title)

    for w in warehouse:
        print(''.join(w))

    print()

def calculate_gps_coordinates(warehouse):
    return sum(100 * i + j for i, row in enumerate(warehouse) for j, col in enumerate(row) if col == '[')

def widen_warehouse(warehouse):
    widened_warehouse = []
    
    robot_position = (-1, -1)    
    
    for row in warehouse:        
        widened_row = []
        for element in row:
            if element == '#':
                widened_row.extend([element, element])
            if element == 'O':
                widened_row.extend(['[', ']'])            
            if element == '.':
                widened_row.extend(['.', '.'])
            if element == '@':
                widened_row.extend(['@', '.'])
                robot_position = (len(widened_warehouse), widened_row.index('@')) 

        widened_warehouse.append(widened_row)

    return widened_warehouse, robot_position
        
if __name__ == "__main__":
    filename = "Day15_test.txt"
    # 1543141
    #filename = "Day15_larger_test.txt"

    with open(filename, 'r') as f:
        lines = f.readlines()
    
    warehouse = []    
    
    i = 0
    for l in lines:
        stripped_line = l.strip()
        if not len(stripped_line):
            break
        
        warehouse.append(list(stripped_line))
        i += 1
        
    cleaned_rows = [row.replace('\n', '') for row in lines[i:]]
    
    moves = "".join(cleaned_rows)
    warehouse, robot_position = widen_warehouse(warehouse)
    
    print("Moves: ", moves)
    print_warehouse("Before Movements", warehouse)

    run_moves(warehouse, moves, robot_position)

    print_warehouse("After Movements", warehouse)

    total_gps_coordinates = calculate_gps_coordinates(warehouse)

    print("Total GPS Coordinates: ", total_gps_coordinates)