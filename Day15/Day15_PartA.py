def calculate_position(move, initial_position):
    move_deltas = {
        '^': (-1, 0),
        'v': (1, 0),
        '<': (0, -1),
        '>': (0, 1),
    }

    dx, dy = move_deltas.get(move)

    return (initial_position[0] + dx, initial_position[1] + dy)

def run_move(warehouse, move, current_position):
    current_symbol = warehouse[current_position[0]][current_position[1]]
    
    peek_position = calculate_position(move, current_position)
    peek_symbol = warehouse[peek_position[0]][peek_position[1]]
    row, col = peek_position

    if not (0 <= row < len(warehouse) and 0 <= col < len(warehouse[0])):
        return current_position

    if peek_symbol == '#':
        return current_position
   
    if peek_symbol == '.':
        warehouse[current_position[0]][current_position[1]] = '.'
        warehouse[row][col] = current_symbol
        return peek_position
    
    # naive solution with recursion
    run_move(warehouse, move, peek_position)
    
    if warehouse[peek_position[0]][peek_position[1]] == '.':
        warehouse[current_position[0]][current_position[1]] = '.'
        warehouse[row][col] = current_symbol
        return peek_position
    
    return current_position
    
def run_moves(warehouse, moves, current_position):
    for move in moves:
        current_position = run_move(warehouse, move, current_position)

def print_warehouse(title, warehouse):
    print(title)

    for w in warehouse:
        print(''.join(w))

    print()

def calculate_gps_coordinates(warehouse):
    return sum(100 * i + j for i, row in enumerate(warehouse) for j, col in enumerate(row) if col == 'O')
        
if __name__ == "__main__":
    #filename = "Day15_test.txt"
    filename = "Day15_larger_test.txt"

    with open(filename, 'r') as f:
        lines = f.readlines()
    
    warehouse = []    
    robot_position = (-1, -1)    

    i = 0
    for l in lines:
        stripped_line = l.strip()
        if not len(stripped_line):
            break

        robot_position = (len(warehouse), l.index('@')) if '@' in stripped_line else robot_position
        warehouse.append(list(stripped_line))
        i += 1
        
    cleaned_rows = [row.replace('\n', '') for row in lines[i:]]
    moves = "".join(cleaned_rows)

    run_moves(warehouse, moves, robot_position)
    total_gps_coordinates = calculate_gps_coordinates(warehouse)

    print("Total GPS Coordinates: ", total_gps_coordinates)